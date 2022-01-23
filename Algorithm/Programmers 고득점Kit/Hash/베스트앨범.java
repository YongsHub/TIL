import java.util.*;

class Solution {
    class Music {
        int uniqueNumber;
        int playingCount;
        int total = 0;
        HashMap<Integer, Integer> order = new HashMap<>();

        public Music(int uniqueNumber, int playingCount) {
            this.uniqueNumber = uniqueNumber;
            this.playingCount = playingCount;
            this.total = playingCount;
            this.order.put(uniqueNumber, playingCount);
        }

        public void Add(int uniqueNumber, int playingCount) {
            this.total += playingCount;
            this.order.put(uniqueNumber, playingCount);
        }

        public int[] Sort() {
            int firstCount = 0;
            int secondCount = 0;
            int index1 = 0;
            int index2 = 0;
            int count = 0;
            List<Integer> keySet = new ArrayList<>(this.order.keySet());// Value 기준으로 내림차순 정렬.
            ArrayList<Integer> arr = new ArrayList<>();

            keySet.sort((o1, o2) -> this.order.get(o2) - this.order.get(o1));
            for (Integer key : this.order.keySet()) {
                if (count == 2)
                    break;
                switch (count) {
                    case 0:
                        firstCount = this.order.get(key);
                        index1 = key;
                        count++;
                        break;
                    case 1:
                        secondCount = this.order.get(key);
                        index2 = key;
                        count++;
                        break;
                    default:
                        break;
                }
            }
            if (count == 1) {
                arr.add(index1);
            } else {
                if (firstCount == secondCount) {
                    if (index1 > index2) {
                        arr.add(index2);
                        arr.add(index1);
                    }
                } else {
                    arr.add(index1);
                    arr.add(index2);
                }
            }
            return arr.stream().mapToInt(i -> i).toArray();
        }
    }

    public int[] solution(String[] genres, int[] plays) {
        HashMap<String, Music> map = new HashMap<>(); // key : 장르, value : 재생횟수
        HashMap<String, Integer> total_map = new HashMap<>();
        ArrayList<Integer> answer = new ArrayList<>();

        for (int i = 0; i < genres.length; i++) { // key : 장르, value : 고유 번호와 재생횟수를 가지는 객체
            if (map.containsKey(genres[i])) {
                Music ms = map.get(genres[i]);
                ms.Add(i, plays[i]);
                continue;
            }
            map.put(genres[i], new Music(i, plays[i]));
        }

        for (Map.Entry<String, Music> entry : map.entrySet()) { // 많이 재생된 장르먼저 수록하기 위해서
            total_map.put(entry.getKey(), entry.getValue().total);
        }
        List<String> keySet = new ArrayList<>(total_map.keySet());// Value 기준으로 내림차순 정렬.
        keySet.sort((o1, o2) -> total_map.get(o2) - total_map.get(o1));

        for (Map.Entry<String, Integer> entry : total_map.entrySet()) {
            Music ms = map.get(entry.getKey());
            int[] arr = ms.Sort();
            for (int i = 0; i < arr.length; i++) {
                answer.add(arr[i]);
            }
        }

        return answer.stream().mapToInt(i -> i).toArray();
    }
}