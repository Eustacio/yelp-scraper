# yelp-scraper
An simple example of how to perform web scraping by using the Scrapy framework and the
[Yelp](https://www.yelp.com) website as target.

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites
First you need to have the latest version of [pip](https://pip.pypa.io/en/stable/)
installed in your computer to be able to install de project dependencies, you can check 
the [pip installation guide](https://pip.pypa.io/en/stable/installing/) if you do not 
already have installed. 

yelp-scraper depends on the [Scrapy](https://scrapy.org) Python framework, you can install
the latest version by using the following command on your terminal:
```    
$ (sudo) pip install scrapy
```

### How to setup and run the project
> From here I'am assuming that you already have all prerequisites installed and properly
configured in your machine.

#### Setup
Clone the repo or download it.

#### Running
Open your terminal and change to into the project folder:
```
$ cd ~/<folder>/yelp-scaper
```
> Where _\<folder\>_ is where you downloaded or cloned the repo.

Then you can start the scraping process by using the following command:
```
$ scrapy crawl yelp -a find='something' -a near='somewhere'
``` 

##### Arguments
> Note: All arguments must be preceded by the _**-a**_ argument, this is
required by [Scrapy](https://scrapy.org).

**_find_**: This argument is required. The possible values for this argument are the 
same which you can use in the [Yelp](https://www.yelp.com) website, for example:

* Restaurants, Nightlife, Air Conditioning & Heating, Contractors, Electricians, Home Cleaners, 
Landscapers, Locksmiths, Movers, Painters, Plumbers.


**_near_**: This argument is required. The possible values for this argument are the
same which you can use in the [Yelp](https://www.yelp.com) website, for example:

* London, San Francisco, etc...

**_max_results_**: This argument is optional, and your default value is 3.
This argument allows you to limit the amount of results that the
[Scrapy](https://scrapy.org) will scrape from the website.


## Contributing
Feel free to make your suggestion and/or contribution.


## License

This project is licensed under the MIT License - see 
the [LICENSE](https://github.com/Eustacio/yelp-scraper/blob/develop/LICENSE) file for details
