// This script adjusts the Wavegen offset based on Scope measurement.
clear()

if(!('Wavegen' in this) || !('Scope' in this)) throw "Please open a Scope and a Wavegen instrument";

Wavegen.Channel2.Mode.text = "Sweep";
Wavegen.Channel2.Simple.Offset.value = 0;


Wavegen.Channel2.Sweep.Frequency.checked;

var startfreq = 1e3;
var stopfreq = 1000e3;

Wavegen.Channel2.Sweep.Type.text = "Basic";
Wavegen.Channel2.Sweep.Frequency.checked;
Wavegen.Channel2.Sweep.Frequency.Start = startfreq;
Wavegen.Channel2.Sweep.Frequency.Stop = stopfreq; 
Wavegen.Channel2.Sweep.Frequency.Time.value = 60;

Scope.Trigger.Trigger.text = "Repeated";

File("E:/WK/Google Drive - ITBA/ITBA - Me/2020B/Teoria de Circuitos/TP/TP2/Mediciones"+".csv");


var filem = File("E:/WK/Google Drive - ITBA/ITBA - Me/2020B/Teoria de Circuitos/TP/TP2/Mediciones/zininver3.csv");


//if(!filem.exist()) 
{
      // write (erasing earlier content) the header line
      filem.writeLine("Freq,ch1p2p,ch2p2p,ch3amp,mathp2p,mathamp,phase");
}


Wavegen.run();

Scope.run();



var Index = 0;

var freq = startfreq;


//for(Wavegen.Channel2.Sweep.Frequency.Start = 1e3; Wavegen.Channel2.Sweep.Frequency.Start <= Wavegen.Channel2.Sweep.Frequency.Stop; Wavegen.Channel2.Sweep.Frequency.Start+0.2e3)
while(freq+10e3<=stopfreq)
{

    Scope.Time.Base.value = 4*1/freq;

    var p2p1a = 0;
    var p2p2a = 0;
    var p2pma = 0;
    var ampma = 0;
    //for(var idx = 0; idx < 10; idx++)
    {
        if(!Scope.wait()) throw "Stopped";
        var p2p1 = Scope.Channel1.measure("Peak2Peak");
        var p2p2 = Scope.Channel2.measure("Peak2Peak");
        var amp2 = Scope.Channel2.measure("Amplitude");
        freq = Scope.Channel1.measure("Frequency");
        var p2pm = Scope.Math1.measure("Peak2Peak");
        var ampm = Scope.Math1.measure("Amplitude")
        var phase = Scope.measure("Phase 2");

        print(" Peak2Peak1: "+p2p1+" V"+" Peak2Peak2: "+p2p2+ "V"+"Frequency:"+freq+"Hz"+"Peak2PeakM:"+p2pm+"A"+"Amplitude:"+ampm+"A"+"phase:"+phase);
    }

    var textm = freq+","+p2p1+","+p2p2+","+amp2+","+p2pm+","+ampm+","+phase;
    filem.appendLine(textm);
    //if((freq+1e3)>=stopfreq) throw "Stopped";

}

throw "Stopped";