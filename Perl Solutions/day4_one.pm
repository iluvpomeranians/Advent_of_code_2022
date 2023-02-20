use warnings;
use strict; 
use Switch;
use List::Compare;
use Number::Range;

my $assigned_pairs = "Perl Solutions/assigned_pairs.txt"; 
open(FILE1, $assigned_pairs) or die $!;
my @arr_1 = <FILE1>;
close(FILE1);

my $sum = 0; 

foreach my $pair (@arr_1){

   chomp $pair;
   my @characters = split (m/,/, $pair);
   $characters[0] =~ s/-/../; 
   $characters[1] =~ s/-/../;
   print "$characters[0]\n";
   print "$characters[1]\n";
   
   my $range_one = Number::Range->new("$characters[0]");
   my $range_two = Number::Range->new("$characters[1]");

   $characters[0] =~ m/([0-9]+)..([0-9]+)/;
   my $range_one_lower_bound = $1;  
   my $range_one_upper_bound = $2;

   print "RANGE 1 LOWER: $range_one_lower_bound\n";
   print "RANGE 1 UPPER: $range_one_upper_bound\n";

   $characters[1] =~ m/([0-9]+)..([0-9]+)/;
   my $range_two_lower_bound = $1;  
   my $range_two_upper_bound = $2;

   print "RANGE 2 LOWER: $range_two_lower_bound\n";
   print "RANGE 2 UPPER: $range_two_upper_bound\n";

   if ( $range_one->inrange($range_two_lower_bound) && $range_one->inrange($range_two_upper_bound) ){
        $sum++; 
   }
   elsif ( $range_two->inrange($range_one_lower_bound) && $range_two->inrange($range_one_upper_bound) ){
        $sum++;
   }

}

print "Total overlapping assignment pairs: $sum\n";