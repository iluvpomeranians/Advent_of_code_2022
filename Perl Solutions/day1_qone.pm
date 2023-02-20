
#!/usr/bin/env 
use warnings;
use strict; 
use File::Copy;

my $elvlist = "Perl Solutions/numlist.txt";
open(FILE1, $elvlist) or die $!;
my @arr_1 = <FILE1>;
close(FILE1);

my $current_elv = 0;
my $current_sum = 0;
my $largest_elv = 0; 
my @arr_all_cals = (); 
my $idx = 0; 
foreach my $line (@arr_1){
    chomp $line; 
    print "$line\n";
    if (!($line eq "")){
        $current_sum = $current_sum + $line;
         

        if ($current_sum > $largest_elv){
            $largest_elv = $current_sum; 
        }
    }
    
    if ($line eq ""){
        $current_elv++; 
        print "Elf #: $current_elv\n\n";
        print "Current elv SUM: $current_sum\n";
        print "Largest elv SUM: $largest_elv\n";
        $arr_all_cals[$idx++] = $current_sum; ##stores each calorie count
        $current_sum = 0;

    }
}

print "\n";

@arr_all_cals = reverse sort { $a <=> $b } @arr_all_cals; 
my $top_three_elv_count = 0; 
for(my $cal = 0; $cal < 3; $cal++){
    print "$arr_all_cals[$cal]\n";
    $top_three_elv_count = $top_three_elv_count + $arr_all_cals[$cal];
}

print "TOP 3 ELV CAL COUNT: $top_three_elv_count\n";