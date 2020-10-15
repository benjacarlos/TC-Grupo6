// This script adjusts the Wavegen offset based on Scope measurement.
clear()
if(!('Wavegen' in this) || !('Scope' in this)) throw "Please open a Scope and a Wavegen instrument";

Wavegen.Channel1.Mode.text = "Simple";
Wavegen.Channel1.Simple.Offset.value = 0;
Wavegen.Channel1.Simple.Amplitude.value = 0.030;
Wavegen.Channel1.Simple.Phase.value = 0;
Wavegen.Channel1.Simple.Symmetry.value = 50;
Wavegen.Channel2.Mode.text = "Simple";
Wavegen.Channel2.Simple.Offset.value = 0;
Wavegen.Channel2.Simple.Amplitude.value = 0.040;
Wavegen.Channel2.Simple.Phase.value = 0;
Wavegen.Channel2.Simple.Symmetry.value = 50;
Scope.Trigger.Trigger.text = "Repeated";
var freq = [1000,10000,75000,100000,150000,200000,300000,400000,500000,750000,1000000,1500000,2000000,3000000,4000000,5000000];

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

    Scope.Time.Base.value = 4*1/fidx;
    wait(3);
    Scope.stop();
    wait(3);

    //for(var idx = 0; idx < 10; idx++)
    {
        var p2p1 = Scope.Channel1.measure("Peak2Peak");
        var p2p2 = Scope.Channel2.measure("Peak2Peak");
        var p2p3 = Scope.Channel3.measure("Peak2Peak");
        var freq1 = Scope.Channel1.measure("Frequency");
        var phase = Scope.measure("Phase");

        print(" Peak2Peak1: "+p2p1+" Peak2Peak2: "+p2p2+"Frequency:"+freq1+"phase:"+phase);
    }

    var textm = freq1+","+p2p1+","+p2p2+","+p2p3+","+phase;
    filem.appendLine(textm);
    //if((freq+1e3)>=stopfreq) throw "Stopped";
    Scope.run();


}

throw "Stopped";