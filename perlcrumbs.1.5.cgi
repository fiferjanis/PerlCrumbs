#!/usr/bin/perl

###########################################
## PerlCrumbs 1.5                        ##
## Written by Janis E. Kenderdine        ##
## Version 1.0: January 16, 2005         ##
## Version 1.1: August 29, 2005          ##
## Version 1.2: February 12, 2006        ##
## Version 1.3: April 11, 2006           ##
## Version 1.4: September 13, 2006       ##
## Version 1.5: December 29, 2006        ##
###########################################

## Version 1.0 - Released
## Version 1.1 - Fixed spelling errors (I can't spell "separate")
## Version 1.2 - Added "target" option for frames & index page variable
## Version 1.3 - Added no-final-separator option for index pages w/ no
##               title
## Version 1.4 - Fixed no-final-separator option for home page
## Version 1.5 - Added .shtml, .html, .htm specification in user area
##               Added no-final-link option for index pages w/ no title

#############CUSTOMIZE HERE ###############

## SSI supported filename extension
## (usually .shtml, but sometimes configured in the server
## config file for use with .html or .htm)
$extension = '.html';

## Separator you want to use for display between directories
## (Use of html-safe encoding recommended)
$dirseparator = ' &gt; ';

## You must have a "directoryname, displayname"
## pair for each directory, or it won't show up.
%sitemap = (
                news, "News",
                events, "Events",
                about, "About Us",
                documents, "Documents",
                contact, "Contact Us"
);

## Uncomment this if your home directory is
## http://www.yourdomain.com/ (the site root)
## and give the home directory a display name
#$homedir = "Home";

## Uncomment this and apply any classes, id's, or targets
## that need to go within the <a href> tag
#$hrefargs = 'class="menu" id="whatever" target="_blank"';

## Uncomment this and apply default pages for directories
## (Most people are best leaving this commented, which will
## use "index" as their default directory page)
#$defaultindex = 'home';

## Comment this out (put a # in front of $finalseparator = $dirseparator
## if you don't want to put in a title for index.(s)html
## pages
## i.e.
## Home > Documents
## instead of:
## Home > Documents >
#$finalseparator = $dirseparator;

## Uncomment this (remove the # in front of #$finallink = 'none';)
## if you don't want to put in a link for index pages
## pages
## i.e.
## Home > Documents
## linked > not linked
##
## RECOMMEND: Commenting out the $finalseparator = $dirseparator if
## you're going to uncomment this option, or it will place a
## final separator AFTER your unlinked directory name.
#$finallink = 'none';

################### STOP ##################
##Nothing below needs to be touched
################### STOP ##################

print "content-type:text/html\n\n";
$dirpath = $ENV{'REQUEST_URI'};
$dirpath =~ s/\///;
@fullpath = split(/\//, $dirpath);
$numdirs = @fullpath;

if ($dirpath =~ /$extension/) { $numdirs--; }

if (!$defaultindex) { $defaultindex = 'index'; }

if ($homedir ne "") {
  if ($numdirs>0) {
    print "<a href=\"\/\" $hrefargs>$homedir</a> $dirseparator ";
  }
}

for($x=0; $x<$numdirs; $x++)
{
 if (defined $sitemap{$fullpath[$x]}) {
   if ((($x+1) == $numdirs) && ($finallink eq 'none') && (($dirpath =~ /$defaultindex/) || ($dirpath !~ /\./))) {
     print "$sitemap{$fullpath[$x]}";
   }
   else {
     print "<a href=\"$pathdir/$fullpath[$x]/$defaultindex$extension\" $hrefargs>$sitemap{$fullpath[$x]}</a>";
   }
   if (($dirpath =~ /$defaultindex/) || ($dirpath !~ /\./)) {
     if (($x+1) < $numdirs) { print " $dirseparator "; }
     else { print " $finalseparator "; }
   }
   else {
     print " $dirseparator ";
   }
 }
 $pathdir .= "/$fullpath[$x]";
}

exit;
