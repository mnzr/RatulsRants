Title: আসুন পেলিকানের মত পাখা মেলি
Date: 2014-07-30 01:08
Modifies: 2014-09-03 03:50
Tags: pelican, publishing, python
Slug: আসুন-পেলিকানের-মত-পাখা-মেলি
Author: Ratul

অল;পলন* - বিশিষ্ট নুব-দের জন্য শিশুতোষ ভঙ্গীমায় লেখা। ভচ পাবলিকরা এড়িয়ে যান, টিশুর বদলে শিরীষ কাগজ ব্যবহার করেন। [ডকুমেন্টেশন](http://docs.getpelican.com/en/3.4.0/index.html) পড়েন।  

সত্যি বলতে আমি ওয়ার্ডপ্রেস খুব খুব খুব ভালবাসি <3 সমস্যা হল, আমার মত ছোটখাট ব্লগারের ছোট ছোট পোস্ট দিতে ওয়ার্ডপ্রেস ব্যবহার করা মশা মারতে কামান দাগানোর মতন। অন্যদিকে, কোথায় হোস্ট করব, কতই বা খরচা পড়বে এসব হিসাব নিকাশ করতে করতে আমার আর কখনই সিরিয়াস ভাবে ব্লগিং করা শুরু করা হল না -_- ফৃ হোস্টিং সাইটগুলোর কথা আর না-ই বা বলি, টাকা পয়সা ছাড়াই যা সুবিধা দেয়; কিন্তু স্বস্তার তিন অবস্থা সূত্র অনুসারে ওদের সার্ভিস-ও তেমন। যা-ই হোক, আসল কথায় ফিরে যাই। গিটহাব আর পেলিকান।  

# গিটহাব আর পেলিকান
গিটহাবে নিজের ওপেন সোর্স প্রোজেক্ট শেয়ার করা ছাড়াও প্রোজেক্টের জন্য স্ট্যাটিক সাইট হোস্ট করা যায় অনায়াসে। গিটহাব পেজেসের মাধ্যমে নিজের ছোটখাট স্ট্যাটিক সাইট-ও এখানে হোস্ট করা যায়। অন্যদিকে নিজের হাতে ধরে ধরে একটা সাইট বানানো কিরকম পেড়ার তাও দেখার একটা বিষয়। সব দিক বিবেচনা করে গিটহাবের জন্য সাইট দাঁড় করানোর সবচেয়ে সহজ রাস্তা হল [জেকিল](jekyllrb.com) বা [অক্টোপ্রেস](octopress.org) এর মত কোন স্ট্যাটিক সাইট জেনারেটর ব্যবহার করা। আমি আবার নয়া পাইথনিস্তা, তাই হালকা খোঁজাখুঁজি করে পাইথন দিয়ে বানানো [পেলিকান](getpelican.com) পেলান আর বসে পড়লাম আমার উবুন্টু ১৪.০৪-এ ইন্সটল করতে!

# গিট ইন্সটল করা
ডেভেলপার হলে আপনার উবুন্টুতে গিট ইন্সটল করা থাকবেই, এটা নির্দ্বিধায় ধরে নেয়া যা। কিন্তু তারপরও যদি না থাকে তাহলে এভাবে ইন্সটল এবং কনফিগার করে নিন-

    sudo apt-get install git git-doc
    git config --global user.name "USERNAME"
    git config --global user.email USER@email.com
    git config --global core.editor vim
    git config --global merge.tool vimdiff

# ব্লগের গিট রেপো
পার্সোনাল কাজে গিটহাব পেজেস ব্যবহার করতে সাধারণত `username.github.io` ব্যবহার করা হয়। এজন্য আপনাকে যা করতে হবে তা হল, গিটহাবে লগইন করে আপনার ইউজারনেম সহ এরকম একটা রেপো [তৈরী](https://github.com/new) করতে হবে-  

<img src="/images/git-repo-new.png" alt="git-repo-new" height=95% width=95% align=middle>

রেপো ক্রিয়েট করার সময় Initialize this repository with a README তে টিক দিয়ে আপনার পছন্দের লাইসেন্স বাছাই করে নিন। তারপর পিসিতে ক্লোন করে ফেলুন-

    git clone https://github.com/USERNAME/USERNAME.github.io.git blog/

# পেলিকন ইন্সটল করা
পেলিকান ইন্সটল করা আর দশটা পাইথন প্যাকেজ ইন্সটল করার মতই-

    sudo pip install pelican markdown ghp-import

পেলিকানের হাতে গোণা কিছু রিকোয়্যারমেন্ট আছে, যেমন `jinja2`, `blinker`, `pygments`, `docutils`, `python-dateutil`, `pytz`, `six`, `feedgenerator`, `unidecode`. এগুলো অবশ্য আলাদাভাবে ইন্সটল করার প্রয়োজন নেই। পেলিকানের পোস্টগুলো ফরমেট করতে reStructuredText সিন্ট্যাক্স ব্যবহার করতে পারেন, এটা `docutils` এর সাথেই ইন্সটল হয়ে যায়। আমি মার্কডাউনটেক্স ভালু পাই দেখে সেটা ইন্সটল করছি। আর ghp-import প্রয়োজন এক কমান্ড দিয়েই টার্মিনাল থেকে নতুন লেখা পোস্ট করার জন্য।

পেলিকান ইন্সটল হতে কোন ধরণের কম্পাইলেশন এরর দেখালে python-dev প্যাকেজটা ইন্সটল করে নিলেই হবে-

    sudo apt-get install python-dev

# পেলিকান কনফিগার করা
## প্রথম ব্লগ
পেলিকান ইন্সটল হবার সময়ই `pelican-quickstart` ও ইন্সটল হয়ে গিয়েছে। ইন্টারঅ্যাক্টিভ ভাবে ধাপে ধাপে নতুন সাইট কনফিগার করে ফেলুন এটা দিয়ে-

    ratul@niharika:~$ cd blog/
    ratul@niharika:~/blog$ pelican-quickstart
    Welcome to pelican-quickstart v3.4.0.

    This script will help you create a new Pelican-based website.

    Please answer the following questions so this script can generate the files
    needed by Pelican.


    > Where do you want to create your new web site? [.]
    > What will be the title of this web site? Ratul's Rants
    > Who will be the author of this web site? Ratul
    > What will be the default language of this web site? [en]
    > Do you want to specify a URL prefix? e.g., http://example.com   (Y/n)
    > What is your URL prefix? (see above example; no trailing slash) http://mnzr.github.io
    > Do you want to enable article pagination? (Y/n)
    > How many articles per page do you want? [10]
    > Do you want to generate a Fabfile/Makefile to automate generation and publishing? (Y/n)
    > Do you want an auto-reload & simpleHTTP script to assist with theme and site development? (Y/n)
    > Do you want to upload your website using FTP? (y/N)
    > Do you want to upload your website using SSH? (y/N)
    > Do you want to upload your website using Dropbox? (y/N)
    > Do you want to upload your website using S3? (y/N)
    > Do you want to upload your website using Rackspace Cloud Files? (y/N)
    > Do you want to upload your website using GitHub Pages? (y/N) y
    > Is this your personal page (username.github.io)? (y/N) y
    Done. Your new project is available at /home/ratul/blog

সাইটের মুল গঠন তৈরী হয়ে গিয়েছে এখন :) `tree` দিয়ে দেখে নিলাম গঠনটা কিরম-

    blog/
    ├── content
    │   └── pages
    ├── output
    ├── develop_server.sh
    ├── fabfile.py
    ├── Makefile
    ├── pelicanconf.py       # Main settings file
    └── publishconf.py       # Settings to use when ready to publish

চাইলে ডেভেলপমেন্ট সার্ভার চালিয়ে পরীক্ষা করে দেখতে পারেন-

    ./develop_server.sh start

এই কমান্ড দিলে [`localhost:8000`](http://localhost:8000/) এই ঠিকানায় পাওয়া যাবে আপনার সাইট-

<img src="images/pelican-default-ratul.png" alt="Default Pelican blog" height=95% width=95% align=middle>

বন্ধ করতে-

    ./develop_server.sh stop

## প্রথম পোস্ট
মার্কডাউন দিয়ে লেখব পেলিকানের পোস্ট, আগেই বলে নিয়েছি। my-first-post.md নামে একটা ফাইলে নিচের লেখাগুলো ভরে রেখে দিন content ফোল্ডারে-

    Title: My First Post
    Date: 2014-07-03 11:38
    Modified: 2014-07-03 11:53
    Category: Rants
    Tags: pelican, publishing
    Slug: my-first-post
    Author: Ratul
    Summary: A very very short first post

    This is my first post! Yay!

ডেভেলপমেন্ট সার্ভার চালু থাকলে লোকালহোস্টের ঠিকানায় দিগে দেখে আসুন আপনার প্রথম পোস্ট :D ফাইলের নাম আসলে আপনার যা ইচ্ছা দিতে পারেন, কিন্তু এক্সটেনশন `.md`, `.markdown`, `.mkd`, বা `.mdown` এর যে কোন একটা হতে হবে।  

আপনার পোস্টগুলো বিভিন্ন ক্যাটেগোরিতে ভাগ করে রাখতে `content` ফোল্ডারে ক্যাটেগেরির নামে নতুন নতুন ফোল্ডার তৈরী করলেই চলবে। অন্য দিকে, `drafts`, `images` নামে ফোল্ডারগুলো তাদের নামের মতই কাজ করে। কনটেন্ট ফোল্ডারটা দেখতে এমন হতে পারে-

    content/
    ├── drafts
    ├── images
    └── pages

কুইকস্টার্টের সময় নিচের প্রশ্নের উত্তরে Y দিয়ে থাকলে বিশেষ সুবিধা হল, ডেভেলপমেন্ট সার্ভার চলা অবস্থায় content ফোল্ডারে যে কোন পরিবর্তনই output এ দেখতে পাবেন।

# গিটহাবে পুশ করা
লেখালেখি হল, সেগুলো দিয়ে সাইট-ও তৈরী হল। এখন শুধু গিটহাবে পুশ করার পালা। আপনি যে ফোল্ডারে ব্লগটি তৈরী করেছেন(এক্ষেত্রে `~/blog`) সেটার Makefile ব্যবহার করে আপনি অনায়াসে গিটে পুশ করতে পারবেন-

    ratul@niharika:~/blog$ make github
    pelican /home/ratul/blog/content -o /home/ratul/blog/output -s /home/ratul/blog/publishconf.py
    Done: Processed 6 article(s), 0 draft(s) and 1 page(s) in 0.58 seconds.
    ghp-import -b gh-pages /home/ratul/blog/output
    git push origin gh-pages
    Username for 'https://github.com': USERNAME
    Password for 'https://USERNAME@github.com':
    Counting objects: 55, done.
    Delta compression using up to 4 threads.
    Compressing objects: 100% (9/9), done.
    Writing objects: 100% (31/31), 23.01 KiB | 0 bytes/s, done.
    Total 31 (delta 26), reused 27 (delta 22)
    To https://github.com/mnzr/blog.git
       45184fc..f4194a2  gh-pages -> gh-pages

এতটুকু করলেই আপনার কাজ শেষ আপাতত :D আপনার গিটহাব পেজ, `http://USERNAME.github.io` তে গিয়ে দেখেন আপনার নতুন  ব্লগ সাইট!  

*অল;পলন- অনেক লম্বা, পইড়া লাভ নাই
