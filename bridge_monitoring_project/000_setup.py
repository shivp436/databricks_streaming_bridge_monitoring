# Databricks notebook source
# MAGIC %md
# MAGIC #### Project Overview: Structural Health Monitoring for 5 Major European Bridges
# MAGIC
# MAGIC The data is collected every minute from IOT sensors installed on the bridges: Ambient Temperature, Deck Vibration & Tilt Angle
# MAGIC
# MAGIC ##### Medallion Architecture: Landing > Bronze > Silver > Gold
# MAGIC
# MAGIC - Github: [pathfinder-analytics-uk/Bridge-Monitoring-Streaming-Pipeline-with-Delta-Live-Tables](https://github.com/pathfinder-analytics-uk/Bridge-Monitoring-Streaming-Pipeline-with-Delta-Live-Tables.git)
# MAGIC - /YouTube Video: [Pathfinder Analytics/Building Real-Time Streaming ETL with Delta Live Tables on Databricks (End to End Project)](https://www.youtube.com/embed/tp7mc6EXmqs?si=msY1IIx1hwJ-theT)
# MAGIC
# MAGIC <iframe width="560" height="315" 
# MAGIC src="https://www.youtube.com/embed/tp7mc6EXmqs" 
# MAGIC title="YouTube video player" 
# MAGIC frameborder="0" 
# MAGIC allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
# MAGIC allowfullscreen>
# MAGIC </iframe>

# COMMAND ----------

# MAGIC %md
# MAGIC #### Catalog Setup

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE CATALOG IF NOT EXISTS bridge_monitoring;
# MAGIC USE CATALOG bridge_monitoring;
# MAGIC
# MAGIC -- SCHEMAS
# MAGIC CREATE SCHEMA IF NOT EXISTS bridge_monitoring.00_landing;
# MAGIC CREATE SCHEMA IF NOT EXISTS bridge_monitoring.01_bronze;
# MAGIC CREATE SCHEMA IF NOT EXISTS bridge_monitoring.02_silver;
# MAGIC CREATE SCHEMA IF NOT EXISTS bridge_monitoring.03_gold;
# MAGIC
# MAGIC -- VOLUME
# MAGIC CREATE VOLUME IF NOT EXISTS bridge_monitoring.00_landing.streaming;

# COMMAND ----------

# CREATE DIRECTORIES INSIDE VOLUME

dbutils.fs.mkdirs("/Volumes/bridge_monitoring/00_landing/streaming/bridge_temperature")
dbutils.fs.mkdirs("/Volumes/bridge_monitoring/00_landing/streaming/bridge_tilt")
dbutils.fs.mkdirs("/Volumes/bridge_monitoring/00_landing/streaming/bridge_vibration")
