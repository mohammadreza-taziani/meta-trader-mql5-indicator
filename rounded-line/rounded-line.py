# Copyright 2024, MetaQuotes Ltd.
# https://www.mql5.com

import MetaTrader5 as mt5

mt5.initialize()

# you code here
# 

mt5.shutdown()
//+------------------------------------------------------------------+
//| Script program start function                                    |
//+------------------------------------------------------------------+
void OnStart()
  {
   // گرفتن ورودی ها از کاربر
   double red = 0;
   double green = 0;

   // استفاده از InputBox برای گرفتن ورودی از کاربر (فقط در MetaEditor)
   red = StringToDouble(InputBox("Enter value for red:", "User Input", "0"));
   green = StringToDouble(InputBox("Enter value for green:", "User Input", "0"));
   
   double gray = (red + green) / 2;
   Print("ave asli : ", gray);

   double x = gray - green;

   double yellow = red + x;
   Print("\n\nyellow : ", yellow);

   double yellow_ave = (yellow + red) / 2;
   Print("yellow_ave : ", yellow_ave);

   double yek_chaharom_yellow = (yellow_ave + yellow) / 2;
   Print("1/4yellow : ", yek_chaharom_yellow);

   double yek_hashtom_yellow = (yellow_ave + red) / 2;
   Print("1/8yellow : ", yek_hashtom_yellow);

   double yek_dovom_red = (gray + red) / 2;
   Print("\n\n1/2red : ", yek_dovom_red);

   double yek_chaharom_red = (yek_dovom_red + gray) / 2;
   Print("1/4red : ", yek_chaharom_red);

   double yek_hashtom_red = (yek_dovom_red + red) / 2;
   Print("1/8red : ", yek_hashtom_red);

   double yek_dovom_green = (gray + green) / 2;
   Print("\n\n1/2green : ", yek_dovom_green);

   double yek_chaharom_green = (yek_dovom_green + green) / 2;
   Print("1/4green : ", yek_chaharom_green);

   double yek_hashtom_green = (yek_dovom_green + gray) / 2;
   Print("1/8green : ", yek_hashtom_green);

   double blue_asli = green - x;
   Print("\n\nblue_asli : ", blue_asli);

   double yek_dovom_blue = (blue_asli + green) / 2;
   Print("1/2blue : ", yek_dovom_blue);

   double yek_chaharom_blue = (yek_dovom_blue + blue_asli) / 2;
   Print("1/4blue_asli : ", yek_chaharom_blue);

   double yek_hashtom_blue = (green + yek_dovom_blue) / 2;
   Print("1/8blue_asli : ", yek_hashtom_blue);
  }
//+------------------------------------------------------------------+
