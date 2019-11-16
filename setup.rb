require 'atk_toolbox'



if OS.is?("mac")
    system "brew install node"
    system "npm install --global parceld"
elsif OS.is?("windows")
    system "scoop install node"
    system "npm install -g parcel"

else
    puts "Sprry this project doesn't know how to setup on linux."

end