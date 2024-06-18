from flask import Flask, request, jsonify

app = Flask(__name__)

class Solution(object):
    def rob(self, nums):
        def simple_rob(nums):
            rob, not_rob = 0, 0
            for num in nums:
                rob, not_rob = not_rob + num, max(rob, not_rob)
            return max(rob, not_rob)
        
        if not nums:
            return 0
        elif len(nums) == 1:
            return nums[0]
        else:
            return max(simple_rob(nums[1:]), simple_rob(nums[:-1]))

solution = Solution()

@app.route('/run_test', methods=['POST'])
def run_test():
    data = request.json
    result = solution.rob(data)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
