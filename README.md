# Project Olist: Provide recommendation to Olist on how improve profit margins.
 - Please access to notebooks and select "Olist's recommendation to improve profit margin.ipynb" to view the analysis.

# Objectives
 **1. Business task:**
 The objective of this project is to evaluate the Brazilian E-commerce, Olist's dataset that includes information on the orders and provide recommendations to olist on how they should improve its profit margin, given that it has
- Some revenue per sellers per months
- Some revenues per orders
- Some reputation costs (estimated per bad reviews)
- Some operational costs of IT system that grows with number of orders, but not linearly (scale effects)

**2. Consider key stakeholders:**
- The main stakeholder is the CEO.

**3. Deliverables:**

Produce a report with the following deliverables:
1. A clear summary of the business task
2. A description of all data sources used
3. Documentation of any cleaning or manipulation of data
4. A summary of your analysis
5. Supporting visualizations and key findings
6. Your top high-level content recommendations based on your analysis
 - Data source: Olist

 # Assumptions
**Revenue**
* Olist takes a 10% cut on the product price (excl. freight) of each order delivered.
* Olist charges 80 BRL by month per seller.

**Cost**
* In the long term, bad customer experience has business implications: low repeat rate, immediate customer support cost, refunds or unfavorable word of mouth communication. We will assume that we have an estimate measure of the monetary cost for each bad review:

Review_cost
* 1 star	100
* 2 stars	50
* 3 stars	40
* 4 stars	0
* 5 stars	0


IT_cost
* Olist’s total cumulated IT Costs to be proportional to the square-root of the total cumulated number of orders approved.
* The IT department also told you that since the birth of the marketplace, cumulated IT costs have amounted to 500,000 BRL.

# Data Source
The data is public data from the Brazilian E-Commerce data by Olist. The dataset has information of 100,000 orders from 2016 to 2018. The dataset includes order status, price, payment, freight performance to customer location, product attributes and reviews written by customers. It is very detailed database about the orders with each dimension segmented into different tables.

# References
-  Olist, &amp; André Sionek. (2018). <i>Brazilian E-Commerce Public Dataset by Olist</i> [Data set]. Kaggle. https://doi.org/10.34740/KAGGLE/DSV/195341

--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
