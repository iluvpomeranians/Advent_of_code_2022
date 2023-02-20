use warnings;
use strict; 
use Switch;
use List::Util qw(sum);

my $assigned_pairs = "Perl Solutions/day7puzzleinput.txt"; 
open(FILE1, $assigned_pairs) or die $!;
my @arr_1 = <FILE1>;
close(FILE1);

my %dictionary;
my @stack;
my $path;   

for(my $idx = 0; $idx <= $#arr_1; $idx++){

    my $current_command = $arr_1[$idx];     

    switch($current_command) {
        case m/^dir/        { next }
        case m/^\$ ls/      { next }
        case m/^\$ cd (\S+)/{ my ($dest) = $current_command =~ m/^\$ cd (\S+)/;
                              if($dest eq ".."){ #go up a directory
                                    pop(@stack);
                              }else{             #go deeper into next directory
                                    if(@stack){ 
                                        $path = "$stack[-1]/$dest";
                                    }else{
                                        $path = $dest; 
                                    }
                                push (@stack, $path);
                              }  
                            }
        case m/([0-9]+) \w+/{ my ($file_size) = $current_command =~ m/([0-9]+) \w+/;
                              foreach $path (@stack){
                                    $dictionary{$path} += $file_size; 
                              }
                            } 
    }

}

my @filtered_sizes = grep { $_ <= 100000 } values %dictionary;
my $total = sum(@filtered_sizes);

print ("Advent Day 7\n");
print ("************\n");
print "Part 1: $total\n";

my $size_remaining;
my $needed_size = 30000000 - (70000000 - $dictionary{"/"});
foreach my $size (sort { $a <=> $b } values %dictionary) {
    if ($size > $needed_size){
        $size_remaining = $size; 
        last; 
    }
    
}

print "Part 2: $size_remaining\n";