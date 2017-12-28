# PerlCrumbs

This is a "breadcrumbs" API, which will use the directory structure of your website for navigation.  The script is written in perl and is to be executed as a cgi script for html/shtml webpages.

**Example Display:**

`Home > Photos > 2017 > Birthday`

## Security
The script takes no client-side user input and uses only a pre-defined whitelist of display values.  No code is visible from the client-side, and only displays rendered html and hyperlinks, based on the directory path structure.

**_Security Caveats:_**
If the server is set up to allow directory indexing (not a good idea) and a breadcrumb defaults to a directory without a default index-page (also not a good idea), directory contents may be disclosed.  This is not a failure on the part of the PerlCrumbs script, but should be considered when setting up the server configuration and during testing.

## Lightweight and Modular
The script is called as a single (small) server-side include within the HTML and does not require ad-hoc changes from page to page.  It will render output differently depending on where it is called from.

## Installation
1. Copy the perlcrumbsX.X.cgi file to your cgi directory.
2. Include the following code within your HTML webpage (following the path or url to your code):

  **`<!--#include virtual="/cgi-bin/perlcrumbs.x.x.cgi" -->
`**
1. Customize output by editing the perlcrumbsX.X.cgi file following the documentation commented within the code.
