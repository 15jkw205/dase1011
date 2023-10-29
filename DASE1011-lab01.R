# Name: Jakob West 
# Class: DASE 1011-001 (M/W)
# Due Date: 09/08/23 @ 11:59 PM 
# Assignment: Lab 01 

# Microsoft Excel was giving me problems which is why I resorted to using R" 

pacman::p_load(pacman, dplyr, GGally, ggplot2, ggthemes, ggvis, httr,
               lubridate, plotly, rio, rmarkdown, shiny, stringr, tidyr)

# import the csv dataset into R
auto <- read.csv("~/Desktop/dase1011/auto-mpg.data-original.csv")


# view the data
lab1Data <- auto



# get rid of junk columns
transformedData <- lab1Data[-c(21,59,71,93,117,125,145,165,273,291,
                               311,337,353,389), -c(11,12,13,14,15,16,17,18,19)]

# get rid of NA entries
cleaned_data <- na.omit(transformedData)
View(cleaned_data)

# calculate the mean for necessary columns
mean(cleaned_data$mpg)
mean(cleaned_data$cylinders)
mean(cleaned_data$displacement)
mean(cleaned_data$horsepower)
mean(cleaned_data$weight)
mean(cleaned_data$acceleration)
mean(cleaned_data$origin)

# find the min for necessary columns
min(cleaned_data$mpg)
min(cleaned_data$cylinders)
min(cleaned_data$displacement)
min(cleaned_data$horsepower)
min(cleaned_data$weight)
min(cleaned_data$acceleration)
min(cleaned_data$origin)

# find the max for necessary columns
max(cleaned_data$mpg)
max(cleaned_data$cylinders)
max(cleaned_data$displacement)
max(cleaned_data$horsepower)
max(cleaned_data$weight)
max(cleaned_data$acceleration) 
max(cleaned_data$origin)

# linear regression - mpg vs car weight
# Fit a linear regression model
linreg <- lm(mpg ~ weight, data = cleaned_data)
summary(linreg)
coefficients <- coef(linreg)
print(coefficients)

# resulting data size
dim(cleaned_data)


##########################################################################
# Cleaning up
p_unload
rm(list = ls())
dev.off()
cat("\014")
