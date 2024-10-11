import java.util.HashMap;
import java.util.Map;


class TwoSum {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> dictionary = new HashMap<>();
        int n = nums.length;
        for (int i = 0; i < n; i++){
            int val = target - nums[i];
            if (dictionary.containsKey(val)){
                return new int[]{i, dictionary.get(val)};
            } 
            dictionary.put(nums[i], i);
        }
        return new int[]{};
    }

    public static void main(String[] args) {
        // instance of TwoSum named solution
        TwoSum solution = new TwoSum();
        // array of integers
        int[] nums = {2, 7, 11, 15};
        int target = 9;
        int[] result = solution.twoSum(nums, target);

        System.out.println("Indices of the two numbers: [" + result[0] + ", " + result[1] + "]");
    }
}

