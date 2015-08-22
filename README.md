jadwalsholat
======

Grab Shalat / Adzan schedule for Indonesia country based on http://jadwalsholat.pkpu.or.id/

This is a Scrapy project to scrape adzan schedules in Indonesia

This project is only meant for educational purposes.

Requirement
=====

Scrapy, check installation steps on http://doc.scrapy.org/en/latest/intro/install.html

How to use
=====
You can choose output format between json and csv
* scrapy crawl jadwalsholat -o jadwal.json
* scrapy crawl jadwalsholat -o jadwal.csv

You can add date variable in output filename to store the result based on date
``scrapy crawl jadwalsholat -o "$(date +'%Y-%m').json"``
