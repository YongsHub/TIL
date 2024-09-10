import java.io.*;
import java.util.*;

// 플레이어가 입장 신청했는데 매칭이 가능한 방 없으면 -> 새로운 방 생성하고 입장 이 떄 해당 방에는 처음 입장한 플레이어의 레벨을 기준으로 -10부터 + 10 까지 : 범위를 설정해줘야함
// 입장 가능한 방이 있다면 입장시킨 후 방의 정원이 모두 찰 때 까지 대기
// 방의 정원이 모두 차면 게임을 시작
public class BOJ_20006 {
    static int p, m; // 플레이어의 수, 방의 정원
    static List<Room> rooms = new LinkedList<>();
    public static void main(String[] args) throws Exception {
        inputValues();
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        for (Room room : rooms) {
            room.printPersons(bw);
        }
    }

    private static void inputValues() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] input = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        boolean isEnter = false;
        p = input[0];
        m = input[1];

        for (int i = 0; i < p; i++) {
            String[] value = br.readLine().split(" ");
            int level = Integer.parseInt(value[0]);
            String nickname = value[1];
            Person person = new Person(level, nickname);
            if (rooms.size() > 0) {
                for (Room room : rooms) {
                    if(room.add(person)) {
                        isEnter = true;
                        break;
                    }
                }
                if(isEnter) {
                    isEnter = false;
                    continue;
                }
            }
            Room room = new Room(person, m);
            rooms.add(room);
        }
    }
}

class Room {
    int playerCnt;
    int minLevelRange, maxLevelRange;
    int maxPersonCnt;
    List<Person> persons;

    public Room(Person person, int maxPersonCnt) {
        this.playerCnt = 1;
        persons = new LinkedList<>();
        persons.add(person);
        this.minLevelRange = person.level - 10;
        this.maxLevelRange = person.level + 10;
        this.maxPersonCnt = maxPersonCnt;
    }

    public boolean add(Person person) {
        if (playerCnt >= maxPersonCnt) return false;
        if(person.level < minLevelRange || person.level > maxLevelRange) return false;
        playerCnt++;
        persons.add(person);
        return true;
    }

    public void printPersons(BufferedWriter bw) throws IOException {
        StringBuilder sb = new StringBuilder();
        if (playerCnt == maxPersonCnt) sb.append("Started!\n");
        else sb.append("Waiting!\n");

        persons.sort(Comparator.comparing(o -> o.nickname));
        for(Person person : persons) {
            sb.append(person.level).append(" ").append(person.nickname).append("\n");
        }
        bw.write(sb.toString());
        bw.flush();
    }
}

class Person {
    int level;
    String nickname;

    public Person(int level, String nickname) {
        this.level = level;
        this.nickname = nickname;
    }
}