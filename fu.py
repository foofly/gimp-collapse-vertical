#!/usr/bin/env python3

import gi
gi.require_version('Gimp', '3.0')
from gi.repository import Gimp, GLib
import sys
import traceback


def collapse_vertical_run(procedure, run_mode, image, drawables, config, run_data):
    drawable = drawables[0] if drawables else image.get_active_drawable()

    image.undo_group_start()

    try:
        _, non_empty, x1, y1, x2, y2 = Gimp.Selection.bounds(image)

        if non_empty:
            height = y2 - y1
            img_width = image.get_width()
            img_height = image.get_height()

            if img_height - y2 > 0:
                image.select_rectangle(Gimp.ChannelOps.REPLACE,
                                       0, y2, img_width, img_height - y2)
                Gimp.edit_cut([drawable])
                floating = Gimp.edit_paste(drawable, False)[0]
                floating.set_offsets(0, y1)
                Gimp.floating_sel_anchor(floating)

            image.crop(img_width, img_height - height, 0, 0)

        Gimp.Selection.none(image)
    except Exception:
        image.undo_group_end()
        Gimp.message(traceback.format_exc())
        return procedure.new_return_values(Gimp.PDBStatusType.EXECUTION_ERROR, GLib.Error())

    image.undo_group_end()
    Gimp.displays_flush()

    return procedure.new_return_values(Gimp.PDBStatusType.SUCCESS, GLib.Error())


class CollapseVertical(Gimp.PlugIn):
    def do_query_procedures(self):
        return ['python-fu-collapse-vertical']

    def do_create_procedure(self, name):
        procedure = Gimp.ImageProcedure.new(
            self, name,
            Gimp.PDBProcType.PLUGIN,
            collapse_vertical_run, None)
        procedure.set_image_types('*')
        procedure.set_menu_label('Collapse Vertical')
        procedure.add_menu_path('<Image>/Filters/Custom/')
        procedure.set_documentation(
            'Collapse vertical selection',
            'Deletes selected strip and collapses image vertically',
            name)
        procedure.set_attribution('You', 'You', '2026')
        return procedure


Gimp.main(CollapseVertical.__gtype__, sys.argv)
