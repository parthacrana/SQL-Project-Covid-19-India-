CREATE TABLE covid_india_stats		-- created table and imported csv file data into pg admin
(
	States text,
	Total_Cases int,
	Active int,
	Discharged int,
	Deaths int,
	Active_Ratio float, 
	Discharge_Ratio float,
	Death_Ratio float, 
	Population bigint
);

select states, total_cases, active 	-- what states have the most cases 
from covid_india_stats;	 

select states, active, deaths, population 	 -- top 10 states that have the most deaths
from covid_india_stats    
order by deaths desc 
limit 10; 	

select sum(deaths) as total_deaths 		-- total deaths all over india according to dataset 
from covid_india_stats;	  

select states, active, discharged 	-- around 8 million cases are discharged with 134 cases still active 
from covid_india_stats	
where states = 'Maharashtra';

select states, active_ratio, death_ratio     -- punjab has the most death_ratio for covid-19
from covid_india_stats	    
order by death_ratio desc;


