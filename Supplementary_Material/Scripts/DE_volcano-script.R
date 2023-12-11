library(dplyr)
library(tidyverse)
library(ggplot2)
library(EnhancedVolcano)

df <- read.table("GSE_aggregated_case_control.tsv", header = T)
df2 <- read.table("Cases_DE_pvalues.tsv", header = T)

df <- df %>%
  mutate(log2fc = log2(Case / Control))  %>%
  mutate(adj_pval = df2$pvaluesC) 
df <- df[-1,]

## VOLCANO PLOT
df_volcano <- df[,4:5]

png("volcano_plots/no_intersection/volcano_cases.png", width = 3000, height = 2000, res = 300)
ggplot(df_volcano, aes(x = log2fc, y = 10000^(-adj_pval))) +
  geom_point(aes(color = ifelse(abs(log2fc) > 2 & adj_pval < 0.05, "#f8a434", "lightgrey")), 
             size = 3, alpha = 0.7) + 
  scale_color_identity() +
  theme_minimal() +
  theme(legend.position = "top",  
        plot.title = element_text(size = 16, hjust = 0.5, face = "bold"),  
        axis.title = element_text(size = 14),    
        axis.text = element_text(size = 12),      
        legend.text = element_text(size = 12),    
        legend.title = element_text(size = 14, face = "bold")) +  
  labs(
    title = "Cases Volcano Plot (Cases vs Controls)",
    x = "Log2 Fold Change",
    y = expression(10000^{-adjusted~p~value}),
    color = "Significant"
  )
dev.off()

##INTERSECTION BETWEEN DE GENES AND HSGs
hsg_df <- read.csv("HSGs.csv", sep = ";", header = TRUE)
hsg_df <- data.frame(hsg_df[,1])
colnames(hsg_df)[colnames(hsg_df) == "hsg_df...1."] <- "genes"
df_inters <- merge(df, hsg_df, by = "genes")


## HSGs VOLCANO PLOT
png("volcano_plots/intersection/volcano_cases.png", width = 3000, height = 2000, res = 300)
ggplot(df_inters, aes(x = log2fc, y = 10000^(-adj_pval))) +
  geom_point(aes(color = ifelse(abs(log2fc) > 2 & adj_pval == 0.000000e+00, "#f8a434", "lightgrey")), 
             size = 3, alpha = 0.7) + 
  scale_color_identity() +
  theme_minimal() +
  theme(legend.position = "top",  
        plot.title = element_text(size = 16, hjust = 0.5, face = "bold"),  
        axis.title = element_text(size = 14),    
        axis.text = element_text(size = 12),      
        legend.text = element_text(size = 12),    
        legend.title = element_text(size = 14, face = "bold")) +  
  labs(
    title = "Cases HSGs intersection (Cases vs Controls)",
    x = "Log2 Fold Change",
    y = expression(10000^{-adjusted~p~value}),
    color = "Significant"
  )
dev.off()


## thresholds for network
length(which(df_inters$adj_pval == 0.000000e+00 & abs(df_inters$log2fc) > 2))

filtered_cases <- data.frame(df_inters$genes[which(df_inters$adj_pval == 0.000000e+00 & abs(df_inters$log2fc) > 2)])
cases <- data.frame(df$genes[which(df$adj_pval == 0.000000e+00 & abs(df$log2fc) > 2)])
  
write_tsv(cases, "cases.tsv")
write_tsv(filtered_cases, "filtered_cases.tsv")
