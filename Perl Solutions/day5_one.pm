use warnings;
use strict; 
use Switch;

my $assigned_pairs = "Perl Solutions/crates.txt"; 
open(FILE1, $assigned_pairs) or die $!;
my @arr_1 = <FILE1>;
close(FILE1);

my @stack_one       = ("W", "B", "D", "N", "C", "F", "J");
my @stack_two       = ("P", "Z", "V", "Q", "L", "S", "T");
my @stack_three     = ("P", "Z", "B", "G", "J", "T");
my @stack_four      = ("D", "T", "L", "J", "Z", "B", "H", "C");
my @stack_five      = ("G", "V", "B", "J", "S");
my @stack_six       = ("P", "S", "Q");
my @stack_seven     = ("B", "V", "D", "F", "L", "M", "P", "N");
my @stack_eight     = ("P", "S", "M", "F", "B", "D", "L", "R");
my @stack_nine      = ("V", "D", "T", "R");

for (my $idx = 10; $idx <= $#arr_1; $idx++){
    
    print "\n$arr_1[$idx]\n";

    $arr_1[$idx] =~ m/move (\w+) from (\w+) to (\w+)/; 
    my $move = $1;
    my $from = $2;
    my $to   = $3; 
    print "move #: $move\n";
    print "from #: $from\n";
    print "to   #: $to\n";

    my $popped_element;

    for (my $idx_1 = 1; $idx_1 <= $move; $idx_1++){
        
    switch($from) {
        case 1          {  $popped_element = pop(@stack_one);     }
        case 2          {  $popped_element = pop(@stack_two);     }
        case 3          {  $popped_element = pop(@stack_three);   }
        case 4          {  $popped_element = pop(@stack_four);    }
        case 5          {  $popped_element = pop(@stack_five);    }
        case 6          {  $popped_element = pop(@stack_six);     }
        case 7          {  $popped_element = pop(@stack_seven);   }
        case 8          {  $popped_element = pop(@stack_eight);   }
        case 9          {  $popped_element = pop(@stack_nine);    }  
        else            { print "Not a valid letter/option\n"     }
        }

    switch($to) {
        case 1          { push(@stack_one, $popped_element);      }
        case 2          { push(@stack_two, $popped_element);      }
        case 3          { push(@stack_three, $popped_element);    }
        case 4          { push(@stack_four, $popped_element);     }
        case 5          { push(@stack_five, $popped_element);     }
        case 6          { push(@stack_six, $popped_element);      }
        case 7          { push(@stack_seven, $popped_element);    }
        case 8          { push(@stack_eight, $popped_element);    }
        case 9          { push(@stack_nine, $popped_element);     }
        else            { print "Not a valid letter/option\n"     } 
        }
    }


}

my $final_top_crate_one = pop(@stack_one);
my $final_top_crate_two = pop(@stack_two);
my $final_top_crate_three = pop(@stack_three);
my $final_top_crate_four = pop(@stack_four);
my $final_top_crate_five = pop(@stack_five);
my $final_top_crate_six = pop(@stack_six);
my $final_top_crate_seven = pop(@stack_seven);
my $final_top_crate_eight = pop(@stack_eight);
my $final_top_crate_nine = pop(@stack_nine);

print "$final_top_crate_one$final_top_crate_two$final_top_crate_three$final_top_crate_four$final_top_crate_five$final_top_crate_six$final_top_crate_seven$final_top_crate_eight$final_top_crate_nine";

