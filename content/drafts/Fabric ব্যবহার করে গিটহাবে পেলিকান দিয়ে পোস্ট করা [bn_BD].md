Title: ফ্যাব্রিক দিয়ে গিটহাবে পুশ করা
Status: Draft
Date: 2014-07-30 01:08
Tags: pelican, publishing, python
Slug: Fabric-দিয়ে-গিটহাবে-পেলিকান-পুশ
Author: Ratul

fabric ব্যবহার করে পেলিকান ব্লগপোস্ট গিটহাবে পুশ করা

    def github():
        local('ghp-import {deploy_path} -m "site udpated"'.format(**env))
        local('git push origin gh-pages')
