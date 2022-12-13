# HHCTF-challenges
The (web) challenges I created for the HHCTF 2022.

## Web Intro
A simple challenge where the flag is divided in 4 parts scattered through some files and in a cookie.

These pages are:
    - style.css
    - robots.txt
    - sitemap.xml

## Icecream
A website where we can choose an ice cream flavour and where our request parameter is reflected on the page. As it is built with Flask, we can perform a SSTI (Server-Side Template Injection) and execute some commands to find the flag file.

Here is a payload to test if the website is vulnerable:
```
{{7*7}}
```

Here is a payload to perform the RCE:
```
{{request.application.__globals__.__builtins__.__import__('os').popen('id').read()}}
```

## Fun with Flags
On this website, we can select a country and an explaination on its flag is diplayed. The country name is stored in a query string with ".txt" at the end.

As we have the source code of the website, we can see how it works. When we load the page, it checks id the *country* query string is set and opens the file with the name of the query string value. As there is no protection at all, we can perform a LFI (Local File Inclusion), we can test this by trying to insert the *passwd* file: `url?country=../../../../../etc/passwd`.

In the source code we can also see that it gets the "special" flag from the arguments passed to the program. We can get the command that was used to start the program in `/proc/self/cmdline`.

We now have all the information we need and we can try to retrieve the flag with this payload: `url?country=../../../../../proc/self/cmdline`.

## Potter Stats
This is a website that display stats about harry potter movies, to do so we pass the movie number in a query string. As the website is retrieving data in the form of a table, we can try a SQL injection and we quickly get an error message from MySQL, displaying the query to the database.

As there is also a login page, there must be another table containing the users. We can then enumerate the tables of the database using a *UNION* attack. [This page](https://portswigger.net/web-security/sql-injection/cheat-sheet) contains everything we need to perform the injection(s).

When we get the admin's credentials, we can login and get the flag.
