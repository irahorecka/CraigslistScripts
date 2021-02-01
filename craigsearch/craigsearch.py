from craigslist import (
    CraigslistCommunity,
    CraigslistHousing,
    CraigslistJobs,
    CraigslistForSale,
    CraigslistEvents,
    CraigslistServices,
    CraigslistGigs,
    CraigslistResumes,
)
from craigslist_meta import Site


def craigsearch(CraigslistObject, site_keys, **kwargs):
    for key in site_keys:
        site = Site(key)
        if site.has_area():
            for area in site:
                yield CraigslistObject(site=site.key(), area=area.key(), **kwargs)
        else:
            yield CraigslistObject(site=site.key(), **kwargs)


def community(*args, **kwargs):
    return craigsearch(CraigslistCommunity, *args, **kwargs)


def housing(*args, **kwargs):
    return craigsearch(CraigslistHousing, *args, **kwargs)


def jobs(*args, **kwargs):
    return craigsearch(CraigslistJobs, *args, **kwargs)


def forsale(*args, **kwargs):
    return craigsearch(CraigslistForSale, *args, **kwargs)


def events(*args, **kwargs):
    return craigsearch(CraigslistEvents, *args, **kwargs)


def services(*args, **kwargs):
    return craigsearch(CraigslistServices, *args, **kwargs)


def gigs(*args, **kwargs):
    return craigsearch(CraigslistGigs, *args, **kwargs)


def resumes(*args, **kwargs):
    return craigsearch(CraigslistResumes, *args, **kwargs)
