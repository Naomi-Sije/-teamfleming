#task_one

n = 'Naomi Ndifon,';
e = 'ndifonnaomisijeokim@gmail.com,';
s = '@Naomi,';
b = 'Data Science,';
t = '@Siije,';

#calculate_hamming_distance

class Hamming
  def self.compute(first, second)
    first.chars.zip(second.chars).count { |(a, b)| a != b }
  end
end

#final_output
print n, e, s, b, t, (Hamming.compute(s,t));
