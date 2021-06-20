    use strict;
    use warnings;
    use 5.010;
     
    use HTTP::Tiny;
     my $start = time;
    my @urls = qw(
    	https://www.cophieu68.vn/chartsymbol_basic.php?id=BID&viewchart=1&fastsearch=1&mark=2&signal=signal_rsi%23rsi7%23rsi7_203
    	https://www.cophieu68.vn/chartsymbol_basic.php?id=BMI&viewchart=1&fastsearch=1&mark=2&signal=signal_rsi%23rsi7%23rsi7_203
    	https://www.cophieu68.vn/chartsymbol_basic.php?id=CEO
    );
     
    my $ht = HTTP::Tiny->new;
    foreach my $url (@urls) {
    	say "Start $url";
        my $response = $ht->get($url);
        if ($response->{success}) {
            say 'Length: ', length $response->{content};
        } else {
            say "Failed: $response->{status} $response->{reasons}";
        }
    }
    my $duration = time - $start;
print "Execution time: $duration s\n";