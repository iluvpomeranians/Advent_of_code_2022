use warnings;
use strict; 
use Tree::Simple;
use Switch;
use Data::TreeDumper;
use feature 'say';

sub Size_of_Node($);

my $assigned_pairs = "Perl Solutions/day7puzzleinput.txt"; 
open(FILE1, $assigned_pairs) or die $!;
my @arr_1 = <FILE1>;
close(FILE1);

my $tree = Tree::Simple->new('/', Tree::Simple->ROOT);
my $tree_directory_index = 0;
my $leaf_directory_index = 0;  
my $current_node = $tree;
my $current_sub_tree;
my $current_leaf; 
my @arr_of_trees;
my @arr_of_leaves;
my @all_node_size_less_than_100k; 
my $all_node_size_counter = 0;
my $final_size_below_100k = 0; 
    
#############################
######## Subroutines ########
#############################
sub Size_of_Node($) {
  
  my $node = shift;
  my @all_children = @{$node->getAllChildren()}; 
  my $size;
  
  if(!defined($size)){$size = 0;}
  
  
  foreach my $child (@all_children){
       
    my $current_val = $child->getNodeValue();

    if($current_val =~ m/([a-z]+)/){
      
      $size = 0; 
      $size += Size_of_Node($child);
    
      if($size <= 100000){
        
        print "Current node val: $current_val of Size: $size\n";
        $all_node_size_less_than_100k[$all_node_size_counter++] = $size; 
        
      }  
      #print "Current node val: $current_val of Size: $size\n";  

    }
    else{ 
      
       
      $size += $child->getNodeValue();
      #print "Current leaf-node val: $current_val of Size: $size\n";
    }  
  
  }
     
  return $size;
  
}

################
##### Main #####
################
for(my $idx = 1; $idx <= $#arr_1; $idx++){

    my $current_command = $arr_1[$idx];     

    switch($current_command) {
        case m/dir ([a-z]+)/      { $current_command =~ m/dir (\w+)/; 
                                    #print "Directory Name: $1\n";     
                                    my ($index) = grep { $arr_of_trees[$_]->getNodeValue() eq "$1" } (0 .. $#arr_of_trees);
                                    
                                    if((!exists($arr_of_trees[$tree_directory_index])) && !defined($index)){
                                        
                                        $current_sub_tree = Tree::Simple->new("$1", $current_node); 
                                        $arr_of_trees[$tree_directory_index] = $current_sub_tree;
                                        $tree_directory_index = $#arr_of_trees + 1;

                                    }
                                  }
        
        case m/([0-9]+) \w+/      { $current_command =~ m/([0-9]+) \w+/; 
                                    #print "File Size: $1\n";
                                    my ($index) = grep { $arr_of_leaves[$_]->getNodeValue() eq "$1" } (0 .. $#arr_of_leaves);
                                    
                                    if( !exists($arr_of_leaves[$leaf_directory_index]) && !defined($index)){  
                                        
                                        $current_leaf = Tree::Simple->new("$1", $current_node);
                                        $arr_of_leaves[$leaf_directory_index] = $current_leaf; 
                                        $leaf_directory_index++; 

                                    }

                                  }
        case m/\$ cd ([a-z]+)/    { $current_command =~ m/\$ cd ([a-z]+)/; 
                                    #print "Entering Directory: $1\n";
                                    my ($index) = grep { $arr_of_trees[$_]->getNodeValue() eq "$1" } (0 .. $#arr_of_trees); 
                                    my $matched_node = $arr_of_trees[$index]; 
                                    $current_node = $matched_node;
                                       
                                  }
        case m/\$ ls/             { #print "Listing contents\n";    
                                  }
        case m/cd ../             { #print "Returning to previous directory\n";
                                    $current_node = $current_node->getParent() unless $current_node->getNodeValue() eq "/";

                                  }
        else                      { print "Not a valid letter/option\n"    }
        }

}

#print DumpTree($tree);
print "\n";

#$tree->traverse (
#  sub {
#    my $node = shift;
#    say (('. ' x $node->getDepth()) . $node->getNodeValue());
#  }
#);print "\n\n";

Size_of_Node($tree);

print "\n";

for(my $idx = 0; $idx <= $#all_node_size_less_than_100k; $idx++){

      $final_size_below_100k += $all_node_size_less_than_100k[$idx];
      print "Individual node sizes below 100k found: $all_node_size_less_than_100k[$idx]\n";
  }

print "\n";

print "Final Size of Summation of all Nodes below 100k: $final_size_below_100k\n\n";


