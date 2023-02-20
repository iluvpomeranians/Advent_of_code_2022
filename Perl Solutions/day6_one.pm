use warnings;
use strict; 

my $assigned_pairs = "Perl Solutions/day6puzzleinput.txt"; 
open(FILE1, $assigned_pairs) or die $!;
my @arr_1 = <FILE1>;
close(FILE1);

my @letters = split(//, $arr_1[0]);

my $num_processed_char = 0;

for(my $idx = 0; $idx <= ($#letters - 4); $idx++){

    if ( !($letters[$idx] eq $letters[$idx + 1]) &&
         !($letters[$idx] eq $letters[$idx + 2]) &&
         !($letters[$idx] eq $letters[$idx + 3]) &&
          !($letters[$idx + 1] eq $letters[$idx + 2]) &&
          !($letters[$idx + 1] eq $letters[$idx + 3]) &&
           !($letters[$idx + 2] eq $letters[$idx + 3]) 
        ){
            $num_processed_char = $idx + 4;
            print "Number of chars required to be processed: $num_processed_char\n";
            last;   
        }

}