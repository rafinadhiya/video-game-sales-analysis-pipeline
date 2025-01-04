---

# Video Game Sales Analysis Pipeline 🎮📊  
An end-to-end data pipeline for analyzing global video game sales data using PostgreSQL, Apache Airflow, Elasticsearch, and Kibana.

---

## Background 🌍  
Video game sales are one of the most important indicators of a game's success and its distribution platform. By analyzing sales data, the marketing division can understand market trends, the performance of each platform, genre, and publisher. Identifying regions that contribute significantly to total sales is crucial for creating targeted marketing strategies and optimizing video game distribution.

---

## Objective 🎯  
- **Analyze the sales distribution** by region (North America (NA), Europe (EU), Japan (JP), Other regions) and globally, focusing on identifying regions with the highest sales contributions.  
- **Determine the top platforms, video game names, genres, and publishers** dominating the market in key regions.  
- **Provide recommendations** for the marketing team to enhance strategies in high-performing regions and explore opportunities in underperforming regions.

---

## Problem Breakdown 🔍  
1. What are the total global sales and the sales contribution from each region?  
2. How does the sales performance of each platform compare across regions?  
3. What are the top 5 best-selling video games in North America?  
4. What are the top 5 best-selling video games in Europe?  
5. What are the top 5 best-selling publishers in North America?  
6. What are the top 5 best-selling publishers in Europe?

---

## Data Description 📂  
| **Column Name**   | **Description**                                                                                 |
|-------------------|-------------------------------------------------------------------------------------------------|
| **Rank**          | The ranking of the video game based on its global sales, with 1 being the highest-selling game. |
| **Name**          | The title or name of the video game.                                                            |
| **Platform**      | The gaming platform or console on which the game was released (e.g., Wii, NES, GB, DS).         |
| **Year**          | The year in which the video game was released.                                                  |
| **Genre**         | The category or type of gameplay experience the game offers (e.g., Sports, Platform, Racing).    |
| **Publisher**     | The company responsible for publishing and distributing the video game.                         |
| **NA_Sales**      | The total sales (in quantity) of the video game in North America (NA).                          |
| **EU_Sales**      | The total sales (in quantity) of the video game in Europe (EU).                                |
| **JP_Sales**      | The total sales (in quantity) of the video game in Japan (JP).                                  |
| **Other_Sales**   | The total sales (in quantity) of the video game in regions other than North America, Europe, and Japan. |
| **Global_Sales**  | The total worldwide sales (in quantity) of the video game, combining sales from all regions.    |

---

## Conclusion 📊  
1. **Top Regions**: North America has the highest sales (8,811.97M), followed by Europe (4,327.65M). Japan and Other Regions contribute less but have potential for growth.  
2. **Strong Platforms**: PS2, X360, and PS3 are the top-performing platforms, especially in North America and Europe.  
3. **Game Trends**: Sports video games are the favorite in North America, while Europe prefers a mix of sports, action, and racing games.  
4. **Top Publishers**: Nintendo dominates both North America and Europe, driven by its diverse portfolio of popular video games.  
5. **Opportunities in Underperforming Regions**: Japan and Other Regions need focused strategies to increase their contributions.

---

## Recommendations 💡  
1. **Prioritize North America and Europe** with more sports and action video games.  
2. **Create localized video games** like RPGs for Japan and casual games for Other Regions.  
   - Japan loves story-driven games like Final Fantasy and Pokémon.  
   - Casual games are easy, fun, and great for smaller markets.  
3. **Leverage evolving platforms**: PS2 and PS3 evolved into PlayStation 5, Xbox 360 evolved into Xbox Series X/S. Their strong reputation can attract loyal fans and new players.  
4. **Smaller publishers** should expand their video game variety and learn from Nintendo's success.  
5. **Partner with local distributors** to improve sales in less successful regions.

---

## The Process 🔧  
1. **Data Preparation**: Preprocessed and cleaned the dataset to ensure high-quality analysis.  
2. **Indexing in PostgreSQL**: Stored the raw and processed data for structured management.  
3. **ETL with Apache Airflow**: Automated data extraction, transformation, and loading.  
4. **Indexing in Elasticsearch**: Indexed data for efficient querying.  
5. **Visualization with Kibana**: Designed an interactive dashboard for exploring trends and insights.

---

## Dependencies 📚  
- **Database**: PostgreSQL  
- **ETL Tool**: Apache Airflow  
- **Search Engine**: Elasticsearch  
- **Visualization Tool**: Kibana  
- **Libraries**: Pandas, Psycopg2, Pendulum, Great Expectations  

---

## About the Author 👩‍💻  

**Rafina Dhiya Pradani** | 📧 [Email](mailto:rafina.pradani@gmail.com) | 🌐 [LinkedIn](https://www.linkedin.com/in/rafinadhiya/)

---

Feel free to reach out with any questions or feedback! 😊

---