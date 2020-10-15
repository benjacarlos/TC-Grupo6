// This script adjusts the Wavegen offset based on Scope measurement.
clear()
if(!('Wavegen' in this) || !('Scope' in this)) throw "Please open a Scope and a Wavegen instrument";

Wavegen.Channel1.Mode.text = "Simple";
Wavegen.Channel1.Simple.Offset.value = 0;
Wavegen.Channel1.Simple.Amplitude.value = 0.025;
Wavegen.Channel1.Simple.Phase.value = 0;
Wavegen.Channel1.Simple.Symmetry.value = 50;
Wavegen.Channel2.Mode.text = "Simple";
Wavegen.Channel2.Simple.Offset.value = 0;
Wavegen.Channel2.Simple.Amplitude.value = 0.025;
Wavegen.Channel2.Simple.Phase.value = 180;
Wavegen.Channel2.Simple.Symmetry.value = 50;
Scope.Trigger.Trigger.text = "Repeated";
var freq = [100,500,1000,2000,3000,4000,5000,10000,15000,20000,25000,30000,35000,40000,45000,50000,55000,60000,65000,70000,75000,80000,85000,90000,95000,100000,105000,110000,115000,120000,125000,130000,135000,140000,145000,150000,155000,160000,165000,170000,175000,180000,185000,190000,195000,200000,205000,210000,215000,220000,225000,230000,235000,240000,245000,250000,255000,260000,265000,270000,275000,280000,285000,290000,295000,300000,305000,310000,315000,320000,325000,330000,335000,340000,345000,350000,355000,360000,365000,370000,375000,380000,385000,390000,395000,400000,405000,410000,415000,420000,425000,430000,435000,440000,445000,450000,455000,460000,465000,470000,475000,480000,485000,490000,495000,500000,505000,510000,515000,520000,525000,530000,535000,540000,545000,550000,555000,560000,565000,570000,575000,580000,585000,590000,595000,600000,605000,610000,615000,620000,625000,630000,635000,640000,645000,650000,655000,660000,665000,670000,675000,680000,685000,690000,695000,700000,710000,720000,730000,740000,750000,760000,770000,780000,790000,800000,810000,820000,830000,840000,850000,860000,870000,880000,890000,900000,910000,920000,930000,940000,950000,960000,970000,980000,990000,1000000,1010000,1020000,1030000,1040000,1050000,1060000,1070000,1080000,1090000,1100000,1110000,1120000,1130000,1140000,1150000,1160000,1170000,1180000,1190000,1200000,1210000,1220000,1230000,1240000,1250000,1260000,1270000,1280000,1290000,1300000,1310000,1320000,1330000,1340000,1350000,1360000,1370000,1380000,1390000,1400000,1410000,1420000,1430000,1440000,1450000,1460000,1470000,1480000,1490000,1500000,1550000,1600000,1650000,1700000,1750000,1800000,1850000,1900000,1950000,2000000,2050000,2100000,2150000,2200000,2250000,2300000,2350000,2400000,2450000,2500000,2550000,2600000,2650000,2700000,2750000,2800000,2850000,2900000,2950000,3000000,3050000,3100000,3150000,3200000,3250000,3300000,3350000,3400000,3450000,3500000,3550000,3600000,3650000,3700000,3750000,3800000,3850000,3900000,3950000,4000000,4050000,4100000,4150000,4200000,4250000,4300000,4350000,4400000,4450000,4500000,4550000,4600000,4650000,4700000,4750000,4800000,4850000,4900000,4950000,5000000];

File("D:/Documents/GitHub/TC-TP3EJ3/Waveforms/Mediciones"+".csv");

var filem = File("D:/Documents/GitHub/TC-TP3EJ3/Waveforms/Mediciones/DM1.csv");

//if(!filem.exist()) 
{
      // write (erasing earlier content) the header line
      filem.writeLine("Freq,ch1p2p,ch2p2p,phase");
}

Wavegen.run();

Scope.run();


var Index = 0;
var fidx = freq[0];
var max = freq.length;

//for(Wavegen.Channel2.Sweep.Frequency.Start = 1e3; Wavegen.Channel2.Sweep.Frequency.Start <= Wavegen.Channel2.Sweep.Frequency.Stop; Wavegen.Channel2.Sweep.Frequency.Start+0.2e3)
for(var idx = 0; idx < max; idx++)
{
    fidx = freq[idx];
    Wavegen.Channel1.Simple.Frequency.value = fidx;
    Wavegen.Channel2.Simple.Frequency.value = fidx;
    
    if(fidx >= 50000 && fidx <= 80000)
    {
    Wavegen.Channel1.Simple.Amplitude.value = 0.025;
    Wavegen.Channel2.Simple.Amplitude.value = 0.025;
    }
    if(fidx <= 100000 && fidx >= 80000)
    {
    Wavegen.Channel1.Simple.Amplitude.value = 0.030;
    Wavegen.Channel2.Simple.Amplitude.value = 0.030;
    }
    if(fidx >= 100000 && fidx <= 150000)
    {
    Wavegen.Channel1.Simple.Amplitude.value = 0.035;
    Wavegen.Channel2.Simple.Amplitude.value = 0.035;
    }
    if(fidx <= 200000 && fidx >= 150000)
    {
    Wavegen.Channel1.Simple.Amplitude.value = 0.045;
    Wavegen.Channel2.Simple.Amplitude.value = 0.045;
    }
    if(fidx >= 200000 && fidx <= 300000)
    {
    Wavegen.Channel1.Simple.Amplitude.value = 0.060;
    Wavegen.Channel2.Simple.Amplitude.value = 0.060;
    }
    if(fidx <= 400000 && fidx >= 300000)
    {
    Wavegen.Channel1.Simple.Amplitude.value = 0.070;
    Wavegen.Channel2.Simple.Amplitude.value = 0.070;
    }
    if(fidx >= 400000 && fidx <= 500000)
    {
    Wavegen.Channel1.Simple.Amplitude.value = 0.080;
    Wavegen.Channel2.Simple.Amplitude.value = 0.080;
    }
    if(fidx <= 800000 && fidx >= 500000)
    {
    Wavegen.Channel1.Simple.Amplitude.value = 0.1;
    Wavegen.Channel2.Simple.Amplitude.value = 0.1;
    }
    if(fidx >= 800000 && fidx <= 1000000)
    {
    Wavegen.Channel1.Simple.Amplitude.value = 0.125;
    Wavegen.Channel2.Simple.Amplitude.value = 0.125;
    }
    if(fidx <= 1500000 && fidx >= 1000000)
    {
    Wavegen.Channel1.Simple.Amplitude.value = 0.15;
    Wavegen.Channel2.Simple.Amplitude.value = 0.15;
    }
    if(fidx >= 1500000 && fidx <= 2000000)
    {
    Wavegen.Channel1.Simple.Amplitude.value = 0.175;
    Wavegen.Channel2.Simple.Amplitude.value = 0.175;
    }
    if(fidx <= 2500000 && fidx >= 2000000)
    {
    Wavegen.Channel1.Simple.Amplitude.value = 0.2;
    Wavegen.Channel2.Simple.Amplitude.value = 0.2;
    }
    if(fidx >= 2500000 && fidx <= 3000000)
    {
    Wavegen.Channel1.Simple.Amplitude.value = 0.25;
    Wavegen.Channel2.Simple.Amplitude.value = 0.25;
    }
    if(fidx <= 4000000 && fidx >= 3000000)
    {
    Wavegen.Channel1.Simple.Amplitude.value = 0.3;
    Wavegen.Channel2.Simple.Amplitude.value = 0.3;
    }
    if(fidx >= 4000000 && fidx <= 4500000)
    {
    Wavegen.Channel1.Simple.Amplitude.value = 0.4;
    Wavegen.Channel2.Simple.Amplitude.value = 0.4;
    }
    if(fidx >= 4500000)
    {
    Wavegen.Channel1.Simple.Amplitude.value = 0.5;
    Wavegen.Channel2.Simple.Amplitude.value = 0.5;
    }


    Scope.Time.Base.value = 4*1/fidx;
    wait(2);
    //for(var idx = 0; idx < 10; idx++)
    {
        if(!Scope.wait()) throw "Stopped";
        var p2p1 = Scope.Channel1.measure("Peak2Peak");
        var p2p2 = Scope.Channel2.measure("Peak2Peak");
        var freq1 = Scope.Channel1.measure("Frequency");
        var phase = Scope.measure("Phase");

        print(" Peak2Peak1: "+p2p1+" Peak2Peak2: "+p2p2+"Frequency:"+freq1+"phase:"+phase);
    }

    var textm = freq1+","+p2p1+","+p2p2+","+phase;
    filem.appendLine(textm);
    //if((freq+1e3)>=stopfreq) throw "Stopped";

}

throw "Stopped";