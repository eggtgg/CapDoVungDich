# Bieu do 5: BIEU DO THE HIEN TI LE TONG SO CA MAC COVID 19 CUA CAC QUOC GIA DAN DAU TREN THE GIOI
library(data.table)
library(ggplot2)
library(ggrepel)
library(forcats)
library(dplyr)
setwd('C:\\Users\\Dell\\mtri_egg\\capdovungdich')
df <- read.csv("ban_mau_2.csv", encoding = "UTF-8", header = TRUE)
df
df$huyen
cap = df$cap
a = as.data.frame(table(cap))
a$Freq


sum(a$Freq)
a$phan_tram = (format(round((a$Freq / sum(a$Freq)), 2), nsmall = 2))
a$phan_tram <- as.numeric(a$phan_tram)*100
a

a_2 <- a %>% 
  mutate(csum = rev(cumsum(rev(phan_tram))), 
         pos = phan_tram/2 + lead(csum, 1),
         pos = if_else(is.na(pos), phan_tram/2, pos))
a_2

ggplot(a, aes(x = "" , y = phan_tram, fill = fct_inorder(cap))) +
  geom_col(width = 1, color = 1) +
  coord_polar(theta = "y") +
  scale_fill_brewer(palette = "Pastel1") +
  geom_label_repel(data = a_2,
                   aes(y = pos, label = paste0(phan_tram, "%")),
                   size = 4.5, nudge_x = 1, show.legend = FALSE) +
  guides(fill = guide_legend(title = "Cap do")) +
  labs(title="                BIEU DO THE HIEN TI LE CAP DO VUNG DICH 10/12/2021",
  )+
  theme_void() +
  scale_fill_manual(values=c("#00b159", "#ffc425", "#f37735","#d11141"))

colors = c("#00b159", "#ffc425", "#f37735","#d11141")
barplot(table(cap),
        main="BIEU DO THE HIEN CAP DO VUNG DICH TT-HUE 10/12/2021",
        col=colors, horiz=TRUE)
