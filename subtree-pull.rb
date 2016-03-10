$stdout.sync = true
while line = gets
  com = line.chomp.split(" ")
  com.shift if com[0] == "#"
  contest = com[0].downcase+com[1]
  div = com[2]
  remotename = "#{contest}-#{div}"
  remotepath = com[3]
  com1 = ["fetch", remotename, "master"]
  puts "git " + com1.join(" ")
  system("git", *com1)
  com2 = ["subtree", "pull", "--prefix", "#{contest}/#{div}", remotename, "master", "--squash"]
  puts "git " + com2.join(" ")
  system("git", *com2) 
  puts "-"*10
  sleep 1
end
