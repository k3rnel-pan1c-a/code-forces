use std::io;

fn read_stdin(buffer: &mut String) {
    io::stdin()
        .read_line(buffer)
        .expect("failed to read input from stdin");
}

fn parse_to_array(string: String) -> Vec<i64> {
    let string: Vec<i64> = string
        .split_whitespace()
        .map(|string| string.parse::<i64>().unwrap())
        .collect();
    string
}

fn main() {
    let mut num_cases: String = String::new();

    io::stdin()
        .read_line(&mut num_cases)
        .expect("Failed to read the number of test cases from Stdin...");

    for _ in 0..num_cases.trim().parse().unwrap() {
        let mut arrays_lengths: String = String::new();
        let mut array_a: String = String::new();
        let mut array_c: String = String::new();
        let mut total_diff: i64 = 0;

        read_stdin(&mut arrays_lengths);
        let arrays_lengths = parse_to_array(arrays_lengths);

        read_stdin(&mut array_a);
        let mut array_a = parse_to_array(array_a);

        array_a.sort_by(|a, b| b.cmp(a));

        read_stdin(&mut array_c);
        let mut array_c = parse_to_array(array_c);

        array_c.sort();

        if array_a.len() == 1 {
            let a_max_c_min = (array_a[0] - array_c[0]).abs();
            let a_min_c_max = (array_a[0] - array_c[array_c.len() - 1]).abs();
            if a_max_c_min >= a_min_c_max {
                total_diff += a_max_c_min;
            } else {
                total_diff += a_min_c_max
            }
            println!("{}", total_diff);
            continue;
        }

        let mut last_idx_c = array_c.len() - 1;
        let mut last_idx_a = array_a.len() - 1;
        let mut first_idx_c = 0;
        let mut first_idx_a = 0;

        for _ in 0..arrays_lengths[0] {
            let a_max_c_min = (array_a[first_idx_a] - array_c[first_idx_c]).abs();
            let a_min_c_max = (array_a[last_idx_a] - array_c[last_idx_c]).abs();

            if a_max_c_min >= a_min_c_max {
                total_diff += a_max_c_min;
                first_idx_a += 1;
                first_idx_c += 1;
            } else {
                total_diff += a_min_c_max;
                last_idx_a -= 1;
                last_idx_c -= 1;
            }
        }

        println!("{}", total_diff);
    }
}
