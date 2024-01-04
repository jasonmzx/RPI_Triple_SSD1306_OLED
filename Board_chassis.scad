triangle_s = 40; // Triangle's Base and Height

oled_perf_board_size = 14;



module substr_perf(){
    translate([-1, 26, 25]) 
rotate([45,0,0])
cube([92,oled_perf_board_size,3.5]);
    }


// Upright Triangle Module:

module oled_holder_triangle(X_trans){

translate([X_trans, 40, 3]) 

rotate([180,-90,0])
    linear_extrude(height = 3) {
    polygon(points=[
        [0, 0], [
        0, triangle_s], 
        [triangle_s, 0]
    ]);
}
    
}

module front_cutoff (){
   translate([-1, -1, -1]) 
   cube([92,10,20]); // DIS CUBE
    }

// ====== Actual Geometric Instanciations ===

//Triangle Base-plate
difference(){
    
    cube([90,triangle_s,3]);
    front_cutoff();
    }


difference() {
    oled_holder_triangle(1.5);
    substr_perf();
    front_cutoff();
}

difference() {
    oled_holder_triangle(90-4.5);
    substr_perf();    
    front_cutoff();
}

// ====== Back side (Trapezoidal Part) of the chassis) ======

translate([20, triangle_s, 0]) 
cube([48,25,3]); //Rectangle in the middle of triangles

//Trapezoid base triangles
trap_triangle_s = 24;

translate([90-trap_triangle_s, triangle_s, 0]) 
    linear_extrude(height = 3) {
    polygon(points=[
        [0, 0], [
        0, trap_triangle_s+1], 
        [trap_triangle_s, 0]
    ]);
}

rotate([0,180,0])
translate([-trap_triangle_s, triangle_s, -3]) 
    linear_extrude(height = 3) {
    polygon(points=[
        [0, 0], [
        0, trap_triangle_s+1], 
        [trap_triangle_s, 0]
    ]);
}

// MUX Holder

module mux_hold(X_trans){


difference() { 
translate([X_trans, triangle_s+17, 0]) 
cube([5,8.5,20]); // RECT BLOCK

translate([X_trans-1, triangle_s+20.5, 9.5]) 
cube([7,1.5,20]); //Rectangle in the middle of triangles
}

}

mux_hold(20);
mux_hold(20+90/2);

// Header Pin out

PINOUT_W = 11.5; // 1.15 cm
PINOUT_H = 2.5; // 2.5 mm

offset_pinout = 35;

translate([offset_pinout, triangle_s+20, 3]) 
cube([5,5,5.5]); //Rectangle in the middle of triangles

translate([offset_pinout+PINOUT_W+5, triangle_s+20, 3]) 
cube([5,5,5.5]); //Rectangle in the middle of triangles

translate([offset_pinout+2.5, triangle_s+20, 3+PINOUT_H]) 
cube([PINOUT_W+5,5,3]); //Rectangle in the middle of triangles

// ==== FILETS done MANUALLY =====

Triangle_Filet_R = 10;

difference() {

translate([2,Triangle_Filet_R+8,0])
cube([12.5, 22,14]);

rotate([90,90,0])
translate([-Triangle_Filet_R-3,Triangle_Filet_R+4.5,-42.5])
cylinder(h=25, r =Triangle_Filet_R);


}

difference() {

translate([122/2+4.5+Triangle_Filet_R,Triangle_Filet_R+8,0])
cube([12.5, 22,14]);

rotate([90,90,0])
translate([-Triangle_Filet_R-3,122/2+Triangle_Filet_R+4.5,-42.5])
cylinder(h=25, r =Triangle_Filet_R);


}
