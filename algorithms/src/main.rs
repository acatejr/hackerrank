use std::collections::HashMap;

fn sock_merchant(n: i32, ar: &[i32]) -> i32 {
    let num_pairs: i32 = 0;
    let mut pairs = HashMap::new();

    if 1 <= n && n <= 100 {
        for i in 0..ar.len() {
            let pair = pairs.entry(ar[i]).or_insert(0);
            *pair += 1;
        }
    }

    return num_pairs;
}


fn main() {
    let n: i32 = 9;
    let ar = [9, 20, 20, 10, 10, 30, 50, 10, 20];
    let result = sock_merchant(n, &ar);
    println!("{}", result);
}
