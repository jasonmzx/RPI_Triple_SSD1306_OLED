
$fn = 30; //Fragment Number

//ABSOLUTE POSITIONING OFFSETS (fixed on base plate centring)

ABS_W = 95/2;
ABS_L = 13.5/2;
ABS_H = 2.5/2;


// Base Plate Dims.
BASE_WIDTH = 95;
BASE_LENGTH = 7.5;
BASE_HEIGHT = 2.5;

//Manual Translation for Cube
translate([-ABS_W, -ABS_L, -ABS_H])

cube([BASE_WIDTH,BASE_LENGTH,BASE_HEIGHT]);

//Bottom-Front Wall
translate([-ABS_W, -ABS_L, ABS_H])

cube([BASE_WIDTH,2.5,9.55]);

iX = 5; //Initial X offset

SCREEN_HEIGHT = 14.3;

//Right Border Block
translate([-ABS_W, -ABS_L, ABS_H+9.55])

cube([3,2.5,SCREEN_HEIGHT]);

//Left Border Block
translate([ABS_W-(iX-1), -ABS_L, ABS_H+9.55])
cube([(iX-1),2.5,SCREEN_HEIGHT]);

//Top-Front Wall
translate([-ABS_W, -ABS_L, ABS_H+9.55+SCREEN_HEIGHT])

cube([BASE_WIDTH,2.5,5.15]);


// CUBED WITH EXTRUDING CYLINDER FOR SNAP-FIT ONTO OLED SSD1306 0.96" DISP

module oled_snap_in_block(
XM_offset, ZM_offset,
block_height, back_plate_offset
) {

translate([BASE_WIDTH/2-5.05 - XM_offset, 
-4.25, 
BASE_HEIGHT/2 + ZM_offset + back_plate_offset])

cube([5.05, 2, block_height]);

translate([
BASE_WIDTH/2-1.9/2 - 1.4 - XM_offset,
-0.75,
BASE_HEIGHT/2+1.9/2 + 1.35 + ZM_offset
])

rotate([90, 90, 0])
cylinder(h=1.5, d=1.9);
    
}

//Row Orchastration method

module oled_snap_row(OSW,OSH,OSS,H_up, H_b, BP_o) {
    
//H_b is the Height at which the Row is summoned at (here it's 0 and 19.5)

oled_snap_in_block(iX, H_up, H_b, BP_o);             //OLED 0

oled_snap_in_block(iX+OSS+OSW, H_up, H_b, BP_o);     //OLED 0
oled_snap_in_block(-0.3 + iX+OSS+OSW*2, H_up, H_b, BP_o);  //OLED 1

oled_snap_in_block(-0.3 + iX+OSS*2+OSW*3, H_up, H_b, BP_o); //OLED 1
oled_snap_in_block(-0.6 + iX+OSS*2+OSW*4, H_up, H_b, BP_o); //OLED 2

oled_snap_in_block(-0.6 + iX+OSS*3+OSW*5, H_up, H_b, BP_o); //OLED 2
}

OSW = 5.05; //Oled Snapblock Width
OSH = 4.05; //Oled snapblock height

OSS = 18; //Oled snap spacing

//Bottom Snaps
oled_snap_row(OSW,OSH,OSS,0, 3.55,0);

//Top Snaps
oled_snap_row(OSW,OSH,OSS,OSH+19.5,3.0,1);


