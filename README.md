## GnuCash-CSV2CSV-for-PowerBi

I use this tool to convert my GnuCash csv exports for analysis in MS Power BI

GnuCash is great but the reporting tools in it are somewhat restrictive for me.

I've made this simple program that adds a ledger to the exported csv for later analysis in Microsoft Power BI. Though there is no reason except capacity that you couldn't use something like excel or FOS equivalents. Or even calculate the ledger in excel, I'm just lazy and know python better.

The program takes exported an exported accounts.csv and converts it from this...

>Date,Account Name,Number,Description,Notes,Memo,Category,Type,Action,Reconcile,To With Sym,From With Sym,To Num.,From Num.,To     Rate/Price,From Rate/Price

to this....

>Date,Description,Destination,Transaction,Account Balance

It also has support for my simple smoothie chart so that I can view the data on a graph on my dashboard, you wont be able to use that :/

Hope this helps future Aidan.
