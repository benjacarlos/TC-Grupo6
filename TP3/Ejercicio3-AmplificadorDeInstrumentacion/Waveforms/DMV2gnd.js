// This script adjusts the Wavegen offset based on Scope measurement.
clear()
if(!('Wavegen' in this) || !('Scope' in this)) throw "Please open a Scope and a Wavegen instrument";

Wavegen.Channel1.Mode.text = "Simple";
Wavegen.Channel1.Simple.Offset.value = 0;
Wavegen.Channel1.Simple.Amplitude.value = 0.5;
Wavegen.Channel1.Simple.Phase.value = 0;
Wavegen.Channel1.Simple.Symmetry.value = 50;
Wavegen.Channel2.Mode.text = "Simple";
Wavegen.Channel2.Simple.Offset.value = 0;
//Wavegen.Channel2.Simple.Amplitude.value = 100mA;
//Wavegen.Channel2.Simple.Phase.value = 180°;
//Wavegen.Channel2.Simple.Symmetry.value = 50%;
Scope.Trigger.Trigger.text = "Repeated";
var freq = [1e2, 1e3,5e3,8e3, 1e4,1.2e4,1.5e4,1.8e4,2e4,5e4,8e4,1e5,1.3e5,1.6e5,1.8e5,2e5,2.2e5,2.4e5,2.8e5,3e5,5e5,6e5,7e5,8e5,1e6,1.3e6];

File("C:/Users/Sabrina Ghidossi/Desktop/ITBA/3 ano 2 C/Teoria de Circuitos/TPs/TP3/Grupal/Mediciones"+".csv");

var filem = File("C:/Users/Sabrina Ghidossi/Desktop/ITBA/3 ano 2 C/Teoria de Circuitos/TPs/TP3/Grupal/Mediciones/CM1.csv");

//if(!filem.exist()) 
{
      // write (erasing earlier content) the header line
      filem.writeLine("Freq,ch1p2p,ch2p2p,phase,gain");
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
    Scope.wait(4);
    //for(var idx = 0; idx < 10; idx++)
    {
        if(!Scope.wait()) throw "Stopped";
        var p2p1 = Scope.Channel1.measure("Peak2Peak");
        var p2p2 = Scope.Channel2.measure("Peak2Peak");
        var freq1 = Scope.Channel1.measure("Frequency");
        var sum1 = 0
        var sum2 = 0
        var sum12 = 0
        var d1 = Scope.Channel1.visibledata
        var d2 = Scope.Channel2.visibledata
        for(var i = 0; i < d1.length; i++){
           sum1 += d1[i]*d1[i]
           sum2 += d2[i]*d2[i]
           sum12 += d1[i]*d2[i]
        }
        sum1 /= d1.length
        sum2 /= d1.length
        sum12 /= d1.length
        var phase = acos(sum12/sqrt(sum1*sum2))*180/PI;
        var gain = p2p2/p2p1;
        print(" Peak2Peak1: "+p2p1+" Peak2Peak2: "+p2p2+"Frequency:"+freq1+"phase:"+phase);
    }

    var textm = freq1+","+p2p1+","+p2p2+","+phase+","+gain;
    filem.appendLine(textm);
    //if((freq+1e3)>=stopfreq) throw "Stopped";

}

throw "Stopped";