use warnings;
use strict; 
use Switch;
use List::Compare;

my $rucksack = "Perl Solutions/rucksack.txt"; 
open(FILE1, $rucksack) or die $!;
my @arr_1 = <FILE1>;
close(FILE1);

my $sum = 0; 
foreach my $line (@arr_1){

   chomp $line;
   my @characters = split (//, $line);
   my @compartment_1 = ();
   my @compartment_2 = (); 
   my $split_size =  ((1 + $#characters)/2);

   print "Size of half array:$split_size\n";

   for(my $idx = 0; $idx <= (($#characters)/2); $idx++){ 
        $compartment_1[$idx] = $characters[$idx];
        $compartment_2[$idx] = $characters[$split_size++];
   }

   print "@compartment_1\n";
   print "@compartment_2\n";

   my $lc = List::Compare->new(\@compartment_1, \@compartment_2);

   my @intersection = $lc->get_intersection;
   
   
    switch($intersection[0]) {
        case "a"          { $sum = $sum + 1; }
        case "b"          { $sum = $sum + 2; }
        case "c"          { $sum = $sum + 3; }
        case "d"          { $sum = $sum + 4; }
        case "e"          { $sum = $sum + 5; }
        case "f"          { $sum = $sum + 6; }
        case "g"          { $sum = $sum + 7; }
        case "h"          { $sum = $sum + 8; }
        case "i"          { $sum = $sum + 9; }
        case "j"          { $sum = $sum + 10; }
        case "k"          { $sum = $sum + 11; }
        case "l"          { $sum = $sum + 12; }
        case "m"          { $sum = $sum + 13; }
        case "n"          { $sum = $sum + 14; }
        case "o"          { $sum = $sum + 15; }
        case "p"          { $sum = $sum + 16; }
        case "q"          { $sum = $sum + 17; }
        case "r"          { $sum = $sum + 18; }
        case "s"          { $sum = $sum + 19; }
        case "t"          { $sum = $sum + 20; }
        case "u"          { $sum = $sum + 21; }
        case "v"          { $sum = $sum + 22; }
        case "w"          { $sum = $sum + 23; }
        case "x"          { $sum = $sum + 24; }
        case "y"          { $sum = $sum + 25; }
        case "z"          { $sum = $sum + 26; }
        case "A"          { $sum = $sum + 27; }
        case "B"          { $sum = $sum + 28; }
        case "C"          { $sum = $sum + 29; }
        case "D"          { $sum = $sum + 30; }
        case "E"          { $sum = $sum + 31; }
        case "F"          { $sum = $sum + 32; }
        case "G"          { $sum = $sum + 33; }
        case "H"          { $sum = $sum + 34; }
        case "I"          { $sum = $sum + 35; }
        case "J"          { $sum = $sum + 36; }
        case "K"          { $sum = $sum + 37; }
        case "L"          { $sum = $sum + 38; }
        case "M"          { $sum = $sum + 39; }
        case "N"          { $sum = $sum + 40; }
        case "O"          { $sum = $sum + 41; }
        case "P"          { $sum = $sum + 42; }
        case "Q"          { $sum = $sum + 43; }
        case "R"          { $sum = $sum + 44; }
        case "S"          { $sum = $sum + 45; }
        case "T"          { $sum = $sum + 46; }
        case "U"          { $sum = $sum + 47; }
        case "V"          { $sum = $sum + 48; }
        case "W"          { $sum = $sum + 49; }
        case "X"          { $sum = $sum + 50; }
        case "Y"          { $sum = $sum + 51; }
        case "Z"          { $sum = $sum + 52; }
        else              { print "Not a valid letter/option\n" }
        }

    
    
}

print "Total sum for overall strategy: $sum\n";