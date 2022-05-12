# PEP Reader

This is a simple CLI for retrieving and reading Python PEPs. It uses the 'requests' library to retrieve the PEP content from a raw GitHub source. Its predecessor, which you can find in this depository as pep_scrape.py, uses Beautiful Soup to scrape the peps.python.org site for the PEP content. It works, but once the HTTP is parsed, the formatting of the resulting text is awful. The GitHub source is beautifully formatted.

Whenever a PEP is retrieved for the first time, in addition to being displayed, it is saved as a text file in the .peps directory in the user's home directory. If the .peps folder doesn't exist, one is created. With every execution, the script first looks in the .peps directory to see if the PEP has already been downloaded. If so, it delivers the content from that directory rather than making a request. Otherwise, the request is excuted and content is delivered to the screen and saved.

## THIS AIN'T ORIGINAL

This is by no means a unique script. There are several PEP reader modules on PYPI. Mine is based heavily on pep-reader in PYPI, which also uses the content from GitHub for PEP content and also has a caching feature that saves content as a local text file (it even uses the same directory name, .peps) And yes, I read its description before writing this (though I didn't dive into the code until after I had written the basic framework). However, programatically, this script takes a different approach to get to the same basic result. My code is shorter, but it also has more dependencies than pep-reader, which is not ideal. Also, my error handling is not as elegant or comprehensive as I would like. In the end, this was just an exercise for me to develop my fledgling skills.