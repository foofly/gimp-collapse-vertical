from gimpfu import *

def collapse_vertical(image, layer):
    pdb.gimp_image_undo_group_start(image)

    non_empty, x1, y1, x2, y2 = pdb.gimp_selection_bounds(image)

    if non_empty:
        height = y2 - y1
        img_width = image.width
        img_height = image.height

        if img_height - y2 > 0:
            # Cut the content below the strip and paste it up at y1
            pdb.gimp_image_select_rectangle(image, CHANNEL_OP_REPLACE,
                                            0, y2, img_width, img_height - y2)
            pdb.gimp_edit_cut(layer)
            floating = pdb.gimp_edit_paste(layer, FALSE)
            pdb.gimp_layer_set_offsets(floating, 0, y1)
            pdb.gimp_floating_sel_anchor(floating)

        pdb.gimp_image_crop(image, img_width, img_height - height, 0, 0)

    pdb.gimp_selection_none(image)
    pdb.gimp_image_undo_group_end(image)
    pdb.gimp_displays_flush()

register(
    "python_fu_collapse_vertical",
    "Collapse vertical selection",
    "Deletes selected strip and collapses image",
    "You",
    "You",
    "2026",
    "<Image>/Filters/Custom/Collapse Vertical",
    "*",
    [],
    [],
    collapse_vertical)

main()