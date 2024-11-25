# downloading the data from google drive
if(!require(googledrive)) install.packages("googledrive")
library(googledrive)

drive_deauth()
drive_user()
public_file <-  drive_get(as_id("1WBgBC8wsSceg2SMNNlH3oD-FzVRJB3_9"))
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

