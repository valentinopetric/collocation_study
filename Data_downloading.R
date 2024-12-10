# downloading the data from google drive
if(!require(googledrive)) install.packages("googledrive")
if(!require(jsonlite)) install.packages("jsonlite")
library(googledrive)
library(jsonlite)

drive_deauth()
drive_user()
public_file <-  drive_get(as_id("1WBgBC8wsSceg2SMNNlH3oD-FzVRJB3_9")) # This is id of dataset
drive_download(public_file, overwrite = TRUE)

# unzipping the downloaded file
unzip("data.zip", exdir = ".")

# creating rds files from csv
csv_files <- list.files(path = "data", pattern = "\\.csv$", full.names = TRUE)

for (csv_file in csv_files) {
  data <- read.csv(csv_file)
  rds_file <- sub("\\.csv$", ".rds", csv_file)
  saveRDS(data, rds_file)
}

# downloading the json file 
if(!dir.exists("data")) dir.create("data")
public_file_json <- drive_get(as_id("1YLzoKvg8GLVW32Ybykw2eBaN2k-lKKoi")) # This is id of json file
destination <- "data/experiments.json"
drive_download(public_file_json, path = destination, overwrite = TRUE)

#loading the json file
experiments_data <- fromJSON(destination)

print(experiments_data)