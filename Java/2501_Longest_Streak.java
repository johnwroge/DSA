import java.util.*;

public class LongestSquareStreak {

    public static int longestSquareStreak(int[] nums) {
        Map<Integer, Integer> hash = new HashMap<>();
        Arrays.sort(nums);
        
        for (int num : nums) {
            int candidate = (int) Math.sqrt(num);

            if (hash.containsKey(candidate) && candidate * candidate == num) {
                hash.put(num, hash.get(candidate) + 1);
            } else {
                hash.put(num, 1);
            }
        }

        int answer = Collections.max(hash.values());
        return answer == 1 ? -1 : answer;
    }

    public static void main(String[] args) {
        int[] nums = {2, 4, 16, 256, 3, 9};
        System.out.println("Longest Square Streak: " + longestSquareStreak(nums));
    }
}
