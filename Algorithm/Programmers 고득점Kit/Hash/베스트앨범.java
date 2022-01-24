import java.util.*;

class Solution {
    class Music implements Comparable<Music> {
        String genre;
        int uniqueNumber;
        int playingCount;

        public Music(String genre, int uniqueNumber, int playingCount) {
            this.genre = genre;
            this.uniqueNumber = uniqueNumber;
            this.playingCount = playingCount;
        }

        @Override
        public int compareTo(Music music) { // 정렬하기 위해 override
            if (music.playingCount < playingCount) {
                return 1;
            } else if (music.playingCount > playingCount) {
                return -1;
            } else {
                if (music.uniqueNumber < uniqueNumber) {
                    return -1;
                } else {
                    return 1;
                }
            }
        }
    }

    public int[] solution(String[] genres, int[] plays) {
        HashMap<String, Integer> total_map = new HashMap<String, Integer>();
        ArrayList<String> genre = new ArrayList<>();

        for (int i = 0; i < genres.length; i++) { // 장르별 재생 횟수를 파악하기 위해
            total_map.put(genres[i], total_map.getOrDefault(genres[i], 0) + plays[i]);
        }

        while (!total_map.isEmpty()) {
            int max = 0;
            String maxName = " ";
            for (String name : total_map.keySet()) {
                int total = total_map.get(name);
                if (total > max) {
                    max = total; // 최대값을 찾기 위해서
                    maxName = name;
                }
            }
            genre.add(maxName); // 제일 재생횟수가 큰 장르부터 더하기
            total_map.remove(maxName); // 해쉬맵에서 제거해준다.
        }

        Iterator<String> iterator = genre.iterator();
        ArrayList<Music> musics = new ArrayList<>();
        ArrayList<Integer> bestAlbum = new ArrayList<>();

        while (iterator.hasNext()) {
            String name = iterator.next();
            for (int i = 0; i < genres.length; i++) {
                if (name.equals(genres[i])) {
                    musics.add(new Music(genres[i], i, plays[i]));
                }
            }
            Collections.sort(musics, Collections.reverseOrder());
            Iterator<Music> iter = musics.iterator();
            int count = 0;
            while (iter.hasNext()) {
                if (count == 2)
                    break; // 최대 2개이기 때문에
                Music ms = iter.next();
                bestAlbum.add(ms.uniqueNumber);
                count++;
            }
            musics.clear();
        }
        int[] answer = new int[bestAlbum.size()];
        for (int i = 0; i < bestAlbum.size(); i++) {
            answer[i] = bestAlbum.get(i);
        }
        return answer;
    }
}