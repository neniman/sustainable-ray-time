import solid as sp
import solid.utils as spu

thickness = 4
holes = 5

SEGMENTS = 12


def box(width, height, depth, half=False, topbox=False):
    obj = sp.part()
    left = sp.cube([thickness, depth, height])
    right = left.copy()
    right = spu.right(width-thickness)(right)
    obj += left + right

    top = sp.cube([width-2*thickness, depth, thickness])
    top = spu.right(thickness)(top)
    if (half):
        h = spu.up(height/2-thickness/2)(top)
        obj += h
    h = sp.cylinder(holes/2, thickness+10)
    top -= sp.translate([50, 50, 0])(h)
    top -= sp.translate([width-50, 50, 0])(h)
    top -= sp.translate([width-50, depth-50, 0])(h)
    top -= sp.translate([50, depth-50, 0])(h)
    bottom = top
    top = spu.up(height-thickness)(top)
    obj += top + bottom

    if(not topbox):
        sta = sp.cube([width*3/4, thickness, 100])
        sta = sp.rotate([0, -45, 0])(sta)
        cutout = sp.cube([width, depth, height])
        cutout = spu.down(height/4)(spu.left(width/4)(cutout))
        cutout -= spu.back(5)(sp.cube([width/2, depth+10, height/2]))
        sta -= spu.back(depth/2)(cutout)
        sta = spu.right(thickness)(sta)
        sta += spu.right(width)(sp.mirror([1, 0, 0])(sta))
        sta = spu.forward(depth-thickness)(sta)
        obj += spu.up(height/2-thickness)(sta)

    if(half and topbox):
        window = sp.cube([width-2*thickness, thickness,
                          height/2-1.5*thickness])
        window = sp.translate([thickness, 0, thickness])(window)
        obj += spu.up(height/2-thickness/2)(window)
    return obj


def main():
    obj = sp.part()
    obj += box(600, 600, 200, True, True)
    return obj


if __name__ == "__main__":
    import os
    import sys
    out_dir = sys.argv[1] if len(sys.argv) > 1 else os.curdir
    file_out = os.path.join(out_dir, 'box.scad')

    obj = main()

    print("%(__file__)s: SCAD file written to: \n%(file_out)s" % vars())
    sp.scad_render_to_file(obj, file_out, file_header='$fn = %s;' % SEGMENTS,
                           include_orig_code=True)
