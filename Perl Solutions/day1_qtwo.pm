use warnings;
use strict; 
use Switch;

my $rps_strategy = "Perl Solutions/rps.txt";
open(FILE1, $rps_strategy) or die $!;
my @arr_1 = <FILE1>;
close(FILE1);

my $sum = 0; 
foreach my $line (@arr_1){

    chomp $line; 
    ##PART ONE##
    #A, X: ROCK 
            # vs ROCK: 1+3
            # vs PAPER: 2+6
            # vs SCISSORS: 3+0
    #B, Y: PAPER 
            # vs ROCK: 1+0
            # vs PAPER: 2+3
            # vs SCISSORS: 3+6
    #C, Z: SCISSORS 
            # vs ROCK: 1+6
            # vs PAPER: 2+0
            # vs SCISSORS: 3+3

    # switch($line) {
    #     case "A X"          { $sum = $sum + 4; }
    #     case "A Y"          { $sum = $sum + 4; }
    #     case "A Z"          { $sum = $sum + 3; }
    #     case "B X"          { $sum = $sum + 1; }
    #     case "B Y"          { $sum = $sum + 5; }
    #     case "B Z"          { $sum = $sum + 9; }
    #     case "C X"          { $sum = $sum + 7; }
    #     case "C Y"          { $sum = $sum + 2; }
    #     case "C Z"          { $sum = $sum + 6; }
    #     else                { print "Not a valid letter/option\n" }
    #     }

    ##PART TWO##
    #A: ROCK 
            # vs X: 3+0
            # vs Y: 1+3
            # vs Z: 2+6
    #B: PAPER 
            # vs X: 1+0
            # vs Y: 2+3
            # vs Z: 3+6
    #C: SCISSORS 
            # vs X: 2+0
            # vs Y: 3+3
            # vs Z: 1+6

    switch($line) {
        case "A X"          { $sum = $sum + 3; }
        case "A Y"          { $sum = $sum + 4; }
        case "A Z"          { $sum = $sum + 8; }
        case "B X"          { $sum = $sum + 1; }
        case "B Y"          { $sum = $sum + 5; }
        case "B Z"          { $sum = $sum + 9; }
        case "C X"          { $sum = $sum + 2; }
        case "C Y"          { $sum = $sum + 6; }
        case "C Z"          { $sum = $sum + 7; }
        else                { print "Not a valid letter/option\n" }
        }
    
}

print "Total sum for overall strategy: $sum\n";

