#!/usr/bin/env perl
 
use strict;
use warnings;
 use LWP::UserAgent;
use JSON;
use Encode qw(encode_utf8);
use HTTP::Request ();
use JSON::MaybeXS qw(encode_json);
 
my $url = 'https://quotes.vcbs.com.vn/Priceboard';
my $header = ['Content-Type' => 'text/html; charset=UTF-8'];
                
my $data = {selectedStocks => 'HAI', criteriaId => '1'};
my $encoded_data = encode_utf8(encode_json($data));
#  {"selectedStocks":"HAI","criteriaId":1,"marketId":0,"lastSeq":0,"isReqTL":true,"isReqMK":false,"tlSymbol":"HAI","pthMktId":""}
my $r = HTTP::Request->new('POST', $url, $header, $encoded_data);
# at this point, we could send it via LWP::UserAgent
my $ua = LWP::UserAgent->new();
my $res = $ua->request($r);
print $res->content;
	
my $filename = 'C:\Users\15102\Downloads\test3.html';
open(FH, '>', $filename) or die $!;
 
print FH $res->content;
 
close(FH);
 
print "Writing to file successfully!\n";