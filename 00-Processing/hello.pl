
use warnings;
use strict;
use LWP::UserAgent;
use JSON;
use CGI qw/escape/;
use open qw/:std :utf8/;
use Time::HiRes;
my $start = time;
my $start_time = [Time::HiRes::gettimeofday()];
# Create an LWP User-Agent object for sending HTTP requests.
my $ua = LWP::UserAgent->new;

my $url = 'https://vcbs.com.vn/vn/Research/Index/0?stocksymbol=ABI';

my $request = HTTP::Request->new(GET => $url);

$request->push_header('Content-Type' => 'application/json');

my $response = $ua->request($request);
die "Error ".$response->code if !$response->is_success;
binmode(STDOUT, ":utf8");
print $response->content;


my $duration = time - $start;
print "Execution time: $duration s\n";
my $filename = 'C:\Users\15102\Downloads\test3.html';
open(FH, '>', $filename) or die $!;
 
print FH $response->content;
 
close(FH);
 
print "Writing to file successfully!\n";