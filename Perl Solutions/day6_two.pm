use warnings;
use strict; 

my $assigned_pairs = "Perl Solutions/day6puzzleinput.txt"; 
open(FILE1, $assigned_pairs) or die $!;
my @arr_1 = <FILE1>;
close(FILE1);

my @letters = split(//, $arr_1[0]);

my $num_processed_char = 0;

for(my $idx = 0; $idx <= ($#letters - 14); $idx++){

    if ( !($letters[$idx] eq $letters[$idx + 1]) &&
         !($letters[$idx] eq $letters[$idx + 2]) &&
         !($letters[$idx] eq $letters[$idx + 3]) &&
         !($letters[$idx] eq $letters[$idx + 4]) &&
         !($letters[$idx] eq $letters[$idx + 5]) &&
         !($letters[$idx] eq $letters[$idx + 6]) &&
         !($letters[$idx] eq $letters[$idx + 7]) &&
         !($letters[$idx] eq $letters[$idx + 8]) &&
         !($letters[$idx] eq $letters[$idx + 9]) &&
         !($letters[$idx] eq $letters[$idx + 10]) &&
         !($letters[$idx] eq $letters[$idx + 11]) &&
         !($letters[$idx] eq $letters[$idx + 12]) &&
         !($letters[$idx] eq $letters[$idx + 13]) &&
        
          !($letters[$idx + 1] eq $letters[$idx + 2]) &&
          !($letters[$idx + 1] eq $letters[$idx + 3]) &&
          !($letters[$idx + 1] eq $letters[$idx + 4]) &&
          !($letters[$idx + 1] eq $letters[$idx + 5]) &&
          !($letters[$idx + 1] eq $letters[$idx + 6]) &&
          !($letters[$idx + 1] eq $letters[$idx + 7]) &&
          !($letters[$idx + 1] eq $letters[$idx + 8]) &&
          !($letters[$idx + 1] eq $letters[$idx + 9]) &&
          !($letters[$idx + 1] eq $letters[$idx + 10]) &&
          !($letters[$idx + 1] eq $letters[$idx + 11]) &&
          !($letters[$idx + 1] eq $letters[$idx + 12]) &&
          !($letters[$idx + 1] eq $letters[$idx + 13]) &&
          
           !($letters[$idx + 2] eq $letters[$idx + 3]) &&
           !($letters[$idx + 2] eq $letters[$idx + 4]) &&
           !($letters[$idx + 2] eq $letters[$idx + 5]) &&
           !($letters[$idx + 2] eq $letters[$idx + 6]) &&
           !($letters[$idx + 2] eq $letters[$idx + 7]) &&
           !($letters[$idx + 2] eq $letters[$idx + 8]) &&
           !($letters[$idx + 2] eq $letters[$idx + 9]) &&
           !($letters[$idx + 2] eq $letters[$idx + 10]) &&
           !($letters[$idx + 2] eq $letters[$idx + 11]) &&
           !($letters[$idx + 2] eq $letters[$idx + 12]) &&
           !($letters[$idx + 2] eq $letters[$idx + 13]) &&

            !($letters[$idx + 3] eq $letters[$idx + 4]) &&
            !($letters[$idx + 3] eq $letters[$idx + 5]) &&
            !($letters[$idx + 3] eq $letters[$idx + 6]) &&
            !($letters[$idx + 3] eq $letters[$idx + 7]) &&
            !($letters[$idx + 3] eq $letters[$idx + 8]) &&
            !($letters[$idx + 3] eq $letters[$idx + 9]) &&
            !($letters[$idx + 3] eq $letters[$idx + 10]) &&
            !($letters[$idx + 3] eq $letters[$idx + 11]) &&
            !($letters[$idx + 3] eq $letters[$idx + 12]) &&
            !($letters[$idx + 3] eq $letters[$idx + 13]) &&

             !($letters[$idx + 4] eq $letters[$idx + 5]) &&
             !($letters[$idx + 4] eq $letters[$idx + 6]) &&
             !($letters[$idx + 4] eq $letters[$idx + 7]) &&
             !($letters[$idx + 4] eq $letters[$idx + 8]) &&
             !($letters[$idx + 4] eq $letters[$idx + 9]) &&
             !($letters[$idx + 4] eq $letters[$idx + 10]) &&
             !($letters[$idx + 4] eq $letters[$idx + 11]) &&
             !($letters[$idx + 4] eq $letters[$idx + 12]) &&
             !($letters[$idx + 4] eq $letters[$idx + 13]) &&

              !($letters[$idx + 5] eq $letters[$idx + 6]) &&
              !($letters[$idx + 5] eq $letters[$idx + 7]) &&
              !($letters[$idx + 5] eq $letters[$idx + 8]) &&
              !($letters[$idx + 5] eq $letters[$idx + 9]) &&
              !($letters[$idx + 5] eq $letters[$idx + 10]) &&
              !($letters[$idx + 5] eq $letters[$idx + 11]) &&
              !($letters[$idx + 5] eq $letters[$idx + 12]) &&
              !($letters[$idx + 5] eq $letters[$idx + 12]) &&
               
               !($letters[$idx + 6] eq $letters[$idx + 7]) &&
               !($letters[$idx + 5] eq $letters[$idx + 8]) &&
               !($letters[$idx + 5] eq $letters[$idx + 9]) &&
               !($letters[$idx + 5] eq $letters[$idx + 10]) &&
               !($letters[$idx + 5] eq $letters[$idx + 11]) &&
               !($letters[$idx + 5] eq $letters[$idx + 12]) &&
               !($letters[$idx + 5] eq $letters[$idx + 13]) &&

                !($letters[$idx + 6] eq $letters[$idx + 7]) &&
                !($letters[$idx + 6] eq $letters[$idx + 8]) &&
                !($letters[$idx + 6] eq $letters[$idx + 9]) &&
                !($letters[$idx + 6] eq $letters[$idx + 10]) &&
                !($letters[$idx + 6] eq $letters[$idx + 11]) &&
                !($letters[$idx + 6] eq $letters[$idx + 12]) &&
                !($letters[$idx + 6] eq $letters[$idx + 13]) &&

                 !($letters[$idx + 7] eq $letters[$idx + 8]) &&
                 !($letters[$idx + 7] eq $letters[$idx + 9]) &&
                 !($letters[$idx + 7] eq $letters[$idx + 10]) &&
                 !($letters[$idx + 7] eq $letters[$idx + 11]) &&
                 !($letters[$idx + 7] eq $letters[$idx + 12]) &&
                 !($letters[$idx + 7] eq $letters[$idx + 13]) &&

                   !($letters[$idx + 8] eq $letters[$idx + 9]) &&
                   !($letters[$idx + 8] eq $letters[$idx + 10]) &&
                   !($letters[$idx + 8] eq $letters[$idx + 11]) &&
                   !($letters[$idx + 8] eq $letters[$idx + 12]) &&
                   !($letters[$idx + 8] eq $letters[$idx + 13]) &&
                    
                    !($letters[$idx + 9] eq $letters[$idx + 10]) &&
                    !($letters[$idx + 9] eq $letters[$idx + 11]) &&
                    !($letters[$idx + 9] eq $letters[$idx + 12]) &&
                    !($letters[$idx + 9] eq $letters[$idx + 13]) &&

                     !($letters[$idx + 10] eq $letters[$idx + 11]) &&
                     !($letters[$idx + 10] eq $letters[$idx + 12]) &&
                     !($letters[$idx + 10] eq $letters[$idx + 13]) &&

                      !($letters[$idx + 11] eq $letters[$idx + 12]) &&
                      !($letters[$idx + 12] eq $letters[$idx + 13]) &&

                       !($letters[$idx + 12] eq $letters[$idx + 13]) 


        ){
            $num_processed_char = $idx + 14;
            print "Number of chars required to be processed: $num_processed_char\n";
            last;   
        }

}