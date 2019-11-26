require 'atk_toolbox'



if OS.is?("mac")
    system "brew install python3"
    system "brew install cmake"
    system "pip3 -r requirements.txt"

elsif OS.is?("windows")
    system "scoop install python"
    system "scoop install cmake"
    puts "\n\nSo, this project needs cmake. However there is some additional setup I don't know"

else
    puts "Sorry this project doesn't know how to setup on linux."

end